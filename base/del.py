from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .modelform import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate



def home(request):
    if request.user.is_authenticated:
        project = Task.objects.filter(user=request.user)
    else:
        project = []    
    context = {'project':project}
    return render(request, 'base/home.html', context)

def createTask(request):
    form = TaskForm()
    if request.Method == 'POST':
        form = TaskForm(request.POST, request.files)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('home')
        else:
            form = TaskForm()
    return render(request, 'base/create_task.html',{'form':form}) 

def viewTask(request,pk):
    project = Task.objects.get(id=pk)
    form = TaskForm(instance = project)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True

def updateTask(request,pk):
    project = Task.objects.get(id=pk)
    if request.Method =='POST':
        form = TaskForm(request.POST,request.FILES,instance=project)
