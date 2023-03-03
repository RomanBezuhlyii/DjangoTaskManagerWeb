from .models import Task
from django.contrib.auth.models import User
from django.db import models
from django.forms import forms, ModelForm, TextInput, Textarea, CharField, PasswordInput, ChoiceField, Select


class TaskForm(ModelForm):

    tasklist = ChoiceField(choices=(),widget=Select(attrs={'class':'form-select'}))

    class Meta:
        model = Task
        fields = ["title",'tasklist','task']
        #Вилучив це поле зі зчитування, задаю його у view
        exclude = ['tasklist']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть опис'
            })
        }

    #Конструктором задаю необхідний перелік варінтів із view
    def __init__(self, *args, **kwargs):
        tasklist = kwargs.pop('tasklist')
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['tasklist'].choices = tasklist


class LoginForm(forms.Form):
    username= CharField(max_length= 25,label="Логін", widget=TextInput(attrs={'class':'form-control w-25 mx-auto','placeholder':'Логін','id':'floatingInput'}))
    password= CharField(max_length= 30, label='Пароль', widget=PasswordInput(attrs={'class':'form-control w-25 mx-auto','placeholder':'Пароль','id':'floatingPassword'}))

'''class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть логін'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть пароль'
            })
        }'''