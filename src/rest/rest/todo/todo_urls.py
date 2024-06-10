from django.urls import path, include
from .todo_controller import TodoListView

urlpatterns = [
    path('',TodoListView().get, name='get_all_todos')
]