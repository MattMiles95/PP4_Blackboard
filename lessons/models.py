from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

LESSON_STATUS = ((0, "Draft"), (1, "Published"))
COMMENT_STATUS = ((0, "Published"), (1, "Reported"))


class Subject(models.Model):
    """
    Creates a single subject.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """
    Stores a single lesson entry related to :model:`auth.user`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subjects')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons')
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    summary = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    lesson_status = models.IntegerField(choices=LESSON_STATUS, default=0)
    
    def formatted_created_on(self):
        return self.created_on.strftime('%d %b. %Y, %I:%M %p')
    
    def formatted_deadline(self):
        return self.deadline.strftime('%d %b. %Y, %I:%M %p')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.user`
    """
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    comment_status = models.IntegerField(choices=COMMENT_STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.created_on.strftime('%d/%m/%Y at %H:%M')} - {
            self.commenter} commented on {
                self.lesson.title}: '{self.body}'"