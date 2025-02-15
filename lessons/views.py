from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Subject, Lesson, Comment
from .forms import CommentForm


def home(request):
    """
    Display the home page.

    **Context**
    None

    **Template:**
    :template:`lessons/index.html`
    """
    return render(request, "lessons/index.html", {})


class EnglishLessons(LoginRequiredMixin, generic.ListView):
    """
    Display an 'infinite scroll' list of active English lessons, ordered by
    most recent first.

    **Context**
    ``object_list``
        A QuerySet of :model:`lessons.Lesson` objects, filtered for:
         - Active status (lesson_status=1)
         - English subject
         - Ordered by creation date (newest first)

    **Template:**
    :template:`lessons/eng.html`
    """
    subject_name = Subject
    queryset = Lesson.objects.filter(
        lesson_status=1,
        subject__name="English"
        ).order_by(
        "-created_on"
    )
    template_name = "lessons/eng.html"


class HistoryLessons(LoginRequiredMixin, generic.ListView):
    """
    Display an 'infinite scroll' list of active History lessons, ordered by
    most recent first.

    **Context**
    ``object_list``
        A QuerySet of :model:`lessons.Lesson` objects, filtered for:
         - Active status (lesson_status=1)
         - History subject
         - Ordered by creation date (newest first)

    **Template:**
    :template:`lessons/hist.html`
    """
    subject_name = Subject
    queryset = Lesson.objects.filter(
        lesson_status=1,
        subject__name="History"
        ).order_by(
        "-created_on"
    )
    template_name = "lessons/hist.html"


class PsychologyLessons(LoginRequiredMixin, generic.ListView):
    """
    Display an 'infinite scroll' list of active Psychology lessons, ordered
    by most recent first.

    **Context**
    ``object_list``
        A QuerySet of :model:`lessons.Lesson` objects, filtered for:
         - Active status (lesson_status=1)
         - Psychology subject
         - Ordered by creation date (newest first)

    **Template:**
    :template:`lessons/psych.html`
    """
    subject_name = Subject
    queryset = Lesson.objects.filter(
        lesson_status=1,
        subject__name="Psychology"
        ).order_by(
        "-created_on"
    )
    template_name = "lessons/psych.html"


@login_required
def lesson_detail(request, slug):
    """
    Display a single :model:`lessons.Lesson` object and handle multiple
    :model:`lessons.Comment` submissions.

    **Context**
    ``lesson``
        The requested :model:`lessons.Lesson` instance
    ``comments``
        QuerySet of comments ordered by creation date
        (:model:`lessons.Comment`)
    ``comment_count``
        Number of approved comments (comment_status=0)
    ``comment_form``
        Instance of :form:`CommentForm`

    **Template:**
    :template:`lessons/lesson_detail.html`
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


def comment_edit(request, slug, comment_id):
    """
    Edit an existing comment, with user ownership verification.

    **Context**

    ``lesson``
        An instance of :model:`lessons.Lesson`.
    ``comment``
        An instance of :model:`lessons.Comment`, related to the lesson.
    """
    if request.method == "POST":

        queryset = Lesson.objects.filter(lesson_status=1)
        lesson = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.commenter == request.user:
            comment = comment_form.save(commit=False)
            comment.lesson = lesson
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Hmm, something went wrong...')

    return HttpResponseRedirect(reverse('lesson_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an existing comment, with user ownership verification.

    **Context**

    ``lesson``
        An instance of :model:`lessons.Lesson`.
    ``comment``
        An instance of :model:`lessons.Comment`, related to the lesson.
    """
    queryset = Lesson.objects.filter(lesson_status=1)
    lesson = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.commenter == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'Hmm, something went wrong...')

    return HttpResponseRedirect(reverse('lesson_detail', args=[slug]))


def comment_report(request, slug, comment_id):
    """
    Report an existing comment, hiding it from users (pending Staff approval).

    **Context**

    ``lesson``
        An instance of :model:`lessons.Lesson`.
    ``comment``
        An instance of :model:`lessons.Comment`, related to the lesson.
    """
    queryset = Lesson.objects.filter(lesson_status=1)
    lesson = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.commenter != request.user:
        comment.lesson = lesson
        comment.comment_status = 1
        comment.save()
        messages.add_message(
            request, messages.SUCCESS, 'Comment reported to your teacher.')
    else:
        messages.add_message(
            request, messages.ERROR, "Hmm, something went wrong...")

    return HttpResponseRedirect(reverse('lesson_detail', args=[slug],))
