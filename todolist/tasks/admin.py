from django.contrib import admin
from .models import Task

# Register the Task model to make it editable in the admin interface
admin.site.register(Task)
