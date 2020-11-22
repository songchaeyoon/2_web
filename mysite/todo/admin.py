from django.contrib import admin
from todo.models import TodoList

# Register your models here.

class TodoListAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_date', 'deadline_date')

admin.site.register(TodoList, TodoListAdmin)
