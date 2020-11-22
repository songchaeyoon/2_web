from django.views.generic import ListView
from todo.models import TodoList


class TodoListLV(ListView):
    model = TodoList