from django.shortcuts import render, redirect
from .forms import HomeworkForm
from .models import Subject, Lesson


def homework_submission(request):
    """
    Renders the homework submission page where users can submit their homework.
    Displays an individual instance of :model:`homework.Submission` and a list of :model:`homework.Subject`.
    **Context**
    ``homework``
        An instance of :model:`homework.Submission`.
    ``subject``
        An instance of :model:`homework.Subject`.
    **Template**
    :template:`homework/homework.html`
    """
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.student = request.user
            submission.save()
            return redirect("home")
    else:
        form = HomeworkForm(initial={"subject": Subject.objects.first()})
        subjects = Subject.objects.all()
        selected_subject_id = request.GET.get('subject')
    if selected_subject_id:
        lessons = Lesson.objects.filter(subject=int(selected_subject_id), lesson_status=1).order_by("title")
    else:
        lessons = Lesson.objects.none()

    return render(
        request,
        "homework/homework.html",
        {
            "form": form,
            "subjects": subjects,
            "lessons": lessons,
        },
    )


def load_lessons(request):
    subject_id = request.GET.get("subject_id")
    lessons = Lesson.objects.filter(subject_id=subject_id, lesson_status=1).order_by("title")
    return render(request, "homework/lessons_dropdown_options.html", {"lessons": lessons})