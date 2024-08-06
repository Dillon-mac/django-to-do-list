from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL pattern for the index view
    path('update_task/<str:pk>/', views.update_task, name='update_task'),  # URL pattern for the update_task view
]