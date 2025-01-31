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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface for the Comment model.
    """
    list_display = ('lesson', 'commenter', 'body', 'created_on', 'comment_status')