from django import forms
from .models import Homework


class HomeworkSubmissionForm(forms.ModelForm):
    """
    Form for submitting homework.
    """
    class Meta:
        model = Homework
        fields = ['lesson', 'content', 'student_notes']

        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Either write out or copy and paste your '
                'homework here.'
                }),
            'student_notes': forms.Textarea(attrs={
                'placeholder': 'Something to add? Leave any comments you '
                'have for your teacher here.'
                })
        }
