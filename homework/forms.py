from django import forms
from lessons.models import Lesson

class HomeworkSubmissionForm(forms.Form):
    lesson_id = forms.ModelChoiceField(
        queryset=Lesson.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select',
            'required': True
        })
    )
    homework_file = forms.FileField(
        required=True,
        allow_empty_file=False,
        validators=[],
        widget=forms.FileInput(attrs={
            'accept': '.pdf,.doc,.docx,.txt',
            'class': 'form-control'
        })
    )
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Add any notes about your submission...'
        })
    )