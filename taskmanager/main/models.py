from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField('Назва', max_length=100)
    task = models.TextField('Завдання')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Всі завдання'
