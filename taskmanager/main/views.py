from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    #tasks = Task.objects.all()
    #Срез количества необходимых записей
    #tasks = Task.object.order_by('id')[:5]
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title':'Головна сторінка', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

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