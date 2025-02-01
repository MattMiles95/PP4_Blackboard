from django.db import models
from lessons.models import Lesson, Subject


class Submission(models.Model):
    """
    Stores a single homework submission.
    """
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    content = models.TextField()
    received_on = models.DateTimeField(auto_now_add=True)
    marked = models.BooleanField(default=False)

    def __str__(self):
        return f"Homework submission by {self.student} for {self.lesson} in {self.subject}"
