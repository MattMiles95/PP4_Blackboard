from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Subject, Lesson, Comment


def home(request):
    return render(request, 'lessons/index.html', {})


class EnglishLessons(generic.ListView):
    """
    Display a list of :model:`lessons.Lesson` objects.
    """
    subject_name = Subject
    queryset = Lesson.objects.filter(status=1, subject__name='English').order_by('-created_on')
    template_name = 'lessons/eng.html'


class HistoryLessons(generic.ListView):
    """
    Display a list of :model:`lessons.Lesson` objects.
    """
    subject_name = Subject
    queryset = Lesson.objects.filter(status=1, subject__name='History').order_by('-created_on')
    template_name = 'lessons/hist.html'


class PsychologyLessons(generic.ListView):
    """
    Display a list of :model:`lessons.Lesson` objects.
    """
    subject_name = Subject
    queryset = Lesson.objects.filter(status=1, subject__name='Psychology').order_by('-created_on')
    template_name = 'lessons/psych.html'


def lesson_detail(request, slug):
    """
    Display a single :model:`lessons.Lesson` object.
    """
    lesson = get_object_or_404(Lesson, slug=slug)
    comments = Comment.objects.filter(lesson=lesson).order_by('-created_on')
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson, 'comments': comments})