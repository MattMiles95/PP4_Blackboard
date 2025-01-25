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
    queryset = Lesson.objects.filter(status=1).order_by('-created_on')
    template_name = 'lessons/eng.html'


class HistoryLessons(generic.ListView):
    """
    Display a list of :model:`lessons.Lesson` objects.
    """
    queryset = Lesson.objects.filter(status=1).order_by('-created_on')
    template_name = 'lessons/hist.html'


class PsychologyLessons(generic.ListView):
    """
    Display a list of :model:`lessons.Lesson` objects.
    """
    queryset = Lesson.objects.filter(status=1).order_by('-created_on')
    template_name = 'lessons/psych.html'
