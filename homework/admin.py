from django.contrib import admin
from .models import Homework


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson', 'subject', 'submitted_at', 'marked')
    list_filter = ('marked', 'submitted_at')
    search_fields = ('student__username', 'lesson__title')
    readonly_fields = ('submitted_at',)
    ordering = ['-submitted_at']