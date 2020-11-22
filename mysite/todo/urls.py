from django.urls import path
from todo.views import TodoListLV


app_name = 'todo'
urlpatterns = [
    path('', TodoListLV.as_view(), name='index'),
]