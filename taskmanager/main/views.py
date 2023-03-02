from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task, TaskList
from .forms import TaskForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import logging
# Create your views here.

@login_required
def index(request):
    #tasks = Task.objects.all()
    #Срез количества необходимых записей
    #tasks = Task.object.order_by('id')[:5]
    #tasks = Task.objects.order_by('id')

    #tasks = Task.objects.filter(user=request.user.id)

    tasklists = TaskList.objects.filter(user = request.user.id)
    context = {
        'title': 'Список листів задач',
        'tasks': tasklists,
        'user': request.user,
        'mode': 'tasklist'
    }

    return render(request, 'main/index.html', context)

def view_tasks(request):
    if request.method == 'POST':
        if request.POST.get('success'):
            delete_task(request,int(request.POST.get('success')))
            return redirect('home')
        elif request.POST.get('edit'):
            request.session['task_id'] = int(request.POST.get('edit'))
            return redirect('edit_task')
    tasks = Task.objects.filter(tasklist__user=request.user.id, tasklist__name='Програмування')
    context = {
        'title': 'Задачі списку {tasklist.name}',
        'tasks': tasks,
        'user': request.user,
        'mode': 'task'
    }
    return render(request,'main/index.html')

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('home')

@login_required
def about(request):
    return render(request, 'main/about.html')

@login_required
def add_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            print(1)
            return redirect('home')
        else:
            error = 'Form don`t valid'
    form = TaskForm()
    new_task = {
        'form': form,
        'page_title': 'Додати завдання'
    }
    return render(request, 'main/add_task.html', new_task)

def edit_task(request):
    task = Task.objects.get(id=request.session['task_id'])
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task.user = request.user
            task.title = form.cleaned_data.get('title')
            task.task = form.cleaned_data.get('task')
            task.save()
            return redirect('home')
        else:
            error = 'Form don`t valid'
    #task = Task.objects.get(id=request.session['task_id'])
    initial_dict = {
        'title': task.title,
        'task': task.task
    }
    form = TaskForm(initial=initial_dict)
    tasks = {
        'form': form,
        'page_title': 'Редагувати завдання'
    }
    return render(request, 'main/add_task.html', tasks)

def login_user(request):
    username = ''
    password = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                context = {'form': form,
                           'error': 'Login or username is incorrect'}
                return render(request, 'main/login.html', context)
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'main/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login_user')

