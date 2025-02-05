from django.contrib import admin
from .models import Homework


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson', 'submitted_at', 'status')
    list_filter = ('status', 'submitted_at')
    search_fields = ('student__username', 'lesson__title', 'notes')
    readonly_fields = ('submitted_at',)
    ordering = ['-submitted_at']