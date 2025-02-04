from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from lessons.models import Subject, Lesson
from .forms import HomeworkSubmissionForm


class HomeworkDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        # Get all subjects
        subjects = Subject.objects.all()
        
        return render(request, 'homework/homework_dashboard.html', {
            'subjects': subjects
        })


class HomeworkSubmissionView(LoginRequiredMixin, View):
    def get(self, request, subject):
        # Get all lessons for the selected subject
        lessons = Lesson.objects.filter(subject__name=subject)
        
        form = HomeworkSubmissionForm()
        form.fields['lesson_id'].queryset = lessons
        
        return render(request, 'homework/homework_submission.html', {
            'form': form,
            'selected_subject': subject
        })