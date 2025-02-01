from django.contrib import admin
from .models import Submission


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    """
    Admin interface for the Submission model.
    """
    list_display = ('student', 'subject', 'lesson', 'received_on', 'marked')
    search_fields = ('student__username', 'subject__name', 'lesson__title')
    date_hierarchy = 'received_on'
    ordering = ['-received_on']