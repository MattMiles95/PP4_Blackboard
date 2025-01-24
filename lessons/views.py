from django.shortcuts import render
from django.http import HttpResponse


def my_lessons(request):
    return HttpResponse("Hello, world.")