from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Subject, Lesson, Comment
from .forms import CommentForm



def home(request):
    return render(request, "lessons/index.html", {})


class EnglishLessons(generic.ListView):
    """
    Display a list of :model:`lessons.Lesson` objects.
    """

    subject_name = Subject
    queryset = Lesson.objects.filter(lesson_status=1, subject__name="English").order_by(
        "-created_on"
    )
    template_name = "lessons/eng.html"


class HistoryLessons(generic.ListView):
    """
    Display a list of :model:`lessons.Lesson` objects.
    """

    subject_name = Subject
    queryset = Lesson.objects.filter(lesson_status=1, subject__name="History").order_by(
        "-created_on"
    )
    template_name = "lessons/hist.html"


class PsychologyLessons(generic.ListView):
    """
    Display a list of :model:`lessons.Lesson` objects.
    """

    subject_name = Subject
    queryset = Lesson.objects.filter(lesson_status=1, subject__name="Psychology").order_by(
        "-created_on"
    )
    template_name = "lessons/psych.html"


def lesson_detail(request, slug):
    """
    Display a single :model:`lessons.Lesson` object.
    """
    
    queryset = Lesson.objects.filter(lesson_status=1)
    lesson = get_object_or_404(queryset, slug=slug)
    comments = lesson.comments.all().order_by("created_on")
    comment_count = lesson.comments.filter(comment_status=0).count()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.lesson = lesson
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 
                "Comment submitted successfully!")
    
    comment_form = CommentForm()

    return render(
        request, "lessons/lesson_detail.html", 
        {
            "lesson": lesson,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )