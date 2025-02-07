from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Lesson, Subject, Comment


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """
    Admin interface for the Subject model.
    """
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin):
    """
    Admin interface for the Lesson model using Django Admin and Summernote.
    """
    list_display = ('title', 'subject', 'teacher', 'lesson_status', 'created_on', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('lesson_status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')

    def save_model(self, request, obj, form, change):
        # Automatically assign current user as teacher for new lessons
        if not obj.pk:
            obj.teacher = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        # Filter lessons to show only those belonging to current teacher
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(teacher=request.user)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface for the Comment model.
    """
    list_display = ('lesson', 'commenter', 'body', 'created_on', 'comment_status')