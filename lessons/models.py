from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons')
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    
    def formatted_created_on(self):
        return self.created_on.strftime('%d %b. %Y, %I:%M %p')
    
    def formatted_deadline(self):
        return self.deadline.strftime('%d %b. %Y, %I:%M %p')

    def __str__(self):
        return f"{self.title} | Lesson created by {self.author}"
    

class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.user`
    """
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.created_on.strftime('%d/%m/%Y at %H:%M')} - {
            self.author} commented on {
                self.lesson.title}: '{self.body}'"