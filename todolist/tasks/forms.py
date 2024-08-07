from django import forms
from .models import Task

# Form to create and edit tasks
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'day', 'completed']