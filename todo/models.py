from django.db import models
from django.utils import timezone




# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=20)
    details=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


