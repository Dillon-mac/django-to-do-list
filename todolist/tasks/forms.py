from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  # Specify the model to use for this form
        fields = ['title']  # Specify the fields to include in the form