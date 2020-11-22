from django.db import models
from django.conf import settings

class Show(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
