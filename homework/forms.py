from django import forms
from .models import Submission
from lessons.models import Lesson


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['subject', 'lesson', 'content']

        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Either write out or copy and paste your homework here.'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lesson'].queryset = Lesson.objects.none()

        if 'subject' in self.data:
            try:
                subject_id = int(self.data.get('subject'))
                self.fields['lesson'].queryset = Lesson.objects.filter(subject_id=subject_id, lesson_status=1).order_by('title')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['lesson'].queryset = self.instance.subject.lesson_set.order_by('title')