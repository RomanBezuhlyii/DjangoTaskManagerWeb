from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TaskList(models.Model):
    name = models.CharField('Назва', max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name} user {self.user}"

    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Списки задач'


class Task(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE, default=1)
    title = models.CharField('Назва', max_length=100)
    task = models.TextField('Завдання')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Всі завдання'
