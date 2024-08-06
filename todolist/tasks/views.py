from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()  # Get all tasks from the database
    form = TaskForm()  # Create an instance of TaskForm
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Populate the form with POST data
        if form.is_valid():
            form.save()  # Save the new task to the database
        return redirect('/')  # Redirect to the index page
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/index.html', context)  # Render the index template with tasks and form

def update_task(request, pk):
    task = Task.objects.get(id=pk)  # Get the task by primary key (id)
    task.completed = not task.completed  # Toggle the task's completion status
    task.save()  # Save the updated task to the database
    return redirect('/')  # Redirect to the index page
