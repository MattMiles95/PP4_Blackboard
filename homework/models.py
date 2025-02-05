from django.db import models
from django.contrib.auth.models import User
from lessons.models import Lesson, Subject

class Homework(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, )
    file = models.FileField(upload_to='homework_files/')
    notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=15,
        choices=[
            ('pending', 'Pending Review'),
            ('marked', 'Marked'),
        ],
        default='pending'
    )

    def __str__(self):
        return f"Homework: {self.lesson.title} by {self.student.username}"

    class Meta:
        ordering = ['-submitted_at']