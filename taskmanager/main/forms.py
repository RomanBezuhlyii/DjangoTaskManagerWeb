from .models import Task
from django.contrib.auth.models import User
from django.forms import forms, ModelForm, TextInput, Textarea, CharField, PasswordInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title",'task']
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