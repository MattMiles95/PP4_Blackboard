from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for submitting a comment.
    """
    class Meta:
        model = Comment
        fields = ('body',)