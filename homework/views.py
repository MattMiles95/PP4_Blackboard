from django.views.generic import View
from django.shortcuts import render, redirect
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
        lessons = Lesson.objects.filter(
            subject__name=subject,
            lesson_status=1)
        form = HomeworkSubmissionForm()
        form.fields['lesson'].queryset = lessons
        return render(request, 'homework/homework_submission.html', {
            'form': form,
            'selected_subject': subject,
        })

    def post(self, request, subject):
        form = HomeworkSubmissionForm(request.POST)
        if form.is_valid():
            homework = form.save(commit=False)
            homework.student = request.user
            homework.subject_id = Subject.objects.get(name=subject).id
            homework.save()
            return redirect('homework_dashboard')
        return render(request, 'homework/homework_submission.html', {
            'form': form,
            'selected_subject': subject
        })