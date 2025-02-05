from django.db import models
from django.contrib.auth.models import User
from lessons.models import Lesson, Subject

class Homework(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, )
    content = models.TextField()
    student_notes = models.TextField(blank=True)
    teacher_notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    marked = models.BooleanField(default=False)

    def __str__(self):
        return f"Homework: {self.lesson.title} by {self.student.username}"

    class Meta:
        ordering = ['-submitted_at']