from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Task
from .modelform import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate

# Create your views here.
@login_required(login_url='login' )
def home(request):
    if request.user.is_authenticated:

        project = Task.objects.filter(user=request.user)
    else:
       project = []    
    context = {'project': project}
    return render(request, 'base/home.html', context)

@login_required(login_url='login' )
def viewTask(request, pk):
    project = Task.objects.get(id=pk)
    form = TaskForm(instance=project)

    # make form read only in view mode
    for field in form.fields.values():
        field.widget.attrs['disabled']= True

    context = {'form': form}
    return render(request, 'base/view_task.html', context)

@login_required(login_url='login')
def createTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('home')
        else:
            form = TaskForm()
    context = {'form': form}
    return render(request,'base/create_task.html', context)


@login_required(login_url='login')
def updateTask(request, pk):
    project = Task.objects.get(id=pk)
    form = TaskForm(instance=project)
    if request.method == 'POST':
        form =TaskForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'base/create_task.html', context )

@login_required(login_url='login' )
def deleteTask(request, pk):
    project = Task.objects.get(id=pk)
    context = {'project': project}
    if request.method == 'POST':
        project.delete()
        return redirect('home')

    return render(request, 'base/task_del_notification.html', context)
