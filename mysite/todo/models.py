from django.db import models
from datetime import date
import datetime

# Create your models here.

class TodoList(models.Model):
    content = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField()

    def __str__(self):
        return f'{self.content} | {self.created_date} | {self.deadline_date}'
