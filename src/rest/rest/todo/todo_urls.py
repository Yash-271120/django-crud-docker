from django.urls import path, include
from .todo_controller import TodoListView
from .todo_controller import TodoDetailView

urlpatterns = [
    path('todos/',TodoListView.as_view(), name='todo-list'),
    path('todos/<str:todo_id>/', TodoDetailView.as_view(), name='todo-detail'),
]