from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_title','description', 'task_complete', 'task_incomplete','task_inprogress']