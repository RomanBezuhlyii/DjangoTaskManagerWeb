from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
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
    tasks = Task.objects.filter(user=request.user.id)
    context = {
        'title': 'Головна сторінка',
        'tasks': tasks,
        'user': request.user
    }
    return render(request, 'main/index.html', context)

@login_required
def about(request):
    return render(request, 'main/about.html')

@login_required
def add_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form don`t valid'
    form = TaskForm()
    new_task = {
        'form': form
    }
    return render(request, 'main/add_task.html', new_task)

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
                return render(request, 'access/login.html', context)
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'access/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login_user')