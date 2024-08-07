from django.db import models

# Model representing a Task
class Task(models.Model):
    # Choices for the day of the week
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    # Task fields: title, description, completion status, and day of the week
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)

    def __str__(self):
        return self.title
