from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task, TaskList
from .forms import TaskForm, LoginForm, TaskListForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import logging
from django.forms import forms, ModelForm, TextInput, Textarea, CharField, PasswordInput, ChoiceField
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
            return redirect(f'/task_in_list?tasklist_id={request.GET["tasklist_id"]}')
        elif request.POST.get('edit'):
            request.session['task_id'] = int(request.POST.get('edit'))
            return redirect('edit_task')
        #elif request.POST.get('add_new'):
            #request.session['tasklist_id'] = int(request.POST.get('add_new'))
    if request.GET['tasklist_id'] == 'all':
        tasks = Task.objects.filter(tasklist__user=request.user.id)
        current_tasklist = 'Всі задачі'
    else:
        tasks = Task.objects.filter(tasklist__user=request.user.id, tasklist__id = int(request.GET['tasklist_id']))
        current_tasklist = TaskList.objects.get(id = int(request.GET['tasklist_id'])).name
    context = {
        'title': f'Задачі списку {current_tasklist}',
        'tasks': tasks,
        'user': request.user,
        'mode': 'task'
    }
    return render(request,'main/index.html', context)

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('home')

@login_required
def about(request):
    return render(request, 'main/about.html')

@login_required
def add_task(request):
    error = ''
    choices = create_choise_list(request.user.id)
    if request.method == 'POST':
        form = TaskForm(request.POST,tasklist=choices)
        if form.is_valid():
            task = form.save(commit=False)
            #form.save()
            #task.user = request.user
            task.tasklist = TaskList.objects.get(id = int(form.cleaned_data.get('tasklist')))
            task.save()
            print(1)
            return redirect('home')
        else:
            error = 'Form don`t valid'
    form = TaskForm(tasklist=choices)
    new_task = {
        'form': form,
        'page_title': 'Додати завдання',
        'choices': choices
    }
    return render(request, 'main/add_task.html', new_task)

def create_choise_list(user_id):
    tasklists = TaskList.objects.filter(user = user_id)
    choise_list = [(elem.id, elem.name) for elem in tasklists]
    return choise_list

@login_required
def edit_task(request):
    task = Task.objects.get(id=request.session['task_id'])
    choices = create_choise_list(request.user.id)
    if request.method == 'POST':
        form = TaskForm(request.POST, tasklist=choices)
        if form.is_valid():
            task.tasklist = TaskList.objects.get(id = int(form.cleaned_data.get('tasklist')))
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
    form = TaskForm(initial=initial_dict,tasklist=choices)
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

@login_required
def add_tasklist(request):
    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            tasklist = form.save(commit=False)
            tasklist.user = request.user
            tasklist.save()
            return redirect('home')
    form = TaskListForm()
    context = {
        'title': 'Новий список задач',
        'page_title': 'Додати новий спсиок задач',
        'form': form
    }
    return render(request, 'main/add_tasklist.html', context)

def tasklist_options(request):

    return render(request, 'main/tasklist_options.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')

