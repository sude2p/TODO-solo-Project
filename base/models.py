from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    task_title = models.CharField(max_length=200)
    description = models.TextField(blank= True, null=True)
    task_complete = models.BooleanField(default=False)
    task_incomplete = models.BooleanField(default=False)
    task_inprogress = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title
