from django.urls import path
from .views import get_tasks, get_task, create_task, update_task, delete_task

urlpatterns = [
    path('tasks/', get_tasks, name='get_tasks'),
    path('tasks/<int:pk>/', get_task, name='get_task'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/update/<int:pk>/', update_task, name='update_task'),
    path('tasks/delete/<int:pk>/', delete_task, name='delete_task'),
]