from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # URL for the task list view
    path('clear/', views.clear_tasks, name='clear_tasks'),  # URL for clearing tasks
]