from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Lesson, Comment


def home(request):
    return render(request, 'lessons/index.html', {})