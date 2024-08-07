from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from collections import defaultdict

# View to list and add tasks
def task_list(request):
    tasks = Task.objects.all().order_by('day')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    # Group tasks by day
    tasks_by_day = defaultdict(list)
    for task in tasks:
        tasks_by_day[task.day].append(task)
    
    # Convert to a sorted list of tuples
    sorted_tasks_by_day = sorted(tasks_by_day.items())

    return render(request, 'todolist/task_list.html', {'tasks_by_day': sorted_tasks_by_day, 'form': form})

# View to clear all tasks for a new week
def clear_tasks(request):
    if request.method == 'POST':
        Task.objects.all().delete()
        return redirect('/')
    return render(request, 'todolist/task_list.html')
