from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from lessons.models import Subject, Lesson
from .forms import HomeworkSubmissionForm


class HomeworkDashboardView(LoginRequiredMixin, View):
    """
    Display the homework dashboard interface.
    
    **Context**
    ``subjects``
        A QuerySet containing all available subjects (:model:`Subject`)
        
    **Template:**
    :template:`homework/homework_dashboard.html`
    """
    def get(self, request):
        subjects = Subject.objects.all()
        
        return render(request, 'homework/homework_dashboard.html', {
            'subjects': subjects
        })


class HomeworkSubmissionView(LoginRequiredMixin, View):
    """
    Handle homework submission with subject-based lesson filtering.
    
    **URL Parameters**
    ``subject``
        Name of the subject whose lessons will be displayed
        
    **GET Method**
    Displays a form for submitting homework, filtered by the specified subject.
    
    **POST Method**
    Processes homework submission form data.
    
    **Context**
    ``form``
        An instance of :form:`HomeworkSubmissionForm`
    ``selected_subject``
        The currently selected subject name
        
    **Messages**
    On successful submission:
    - Success message: "Homework submitted, good job!"
    On failed submission:
    - Error message: "Hmm, something went wrong..."
        
    **Template:**
    :template:`homework/homework_submission.html`
    """
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
            messages.add_message(request, messages.SUCCESS, 'Homework submitted, good job!')
            return redirect('homework_dashboard')
        else:
            messages.add_message(request, messages.ERROR, 'Hmm, something went wrong...')
            
        return render(request, 'homework/homework_dashboard.html', {
            'form': form,
            'selected_subject': subject
        })