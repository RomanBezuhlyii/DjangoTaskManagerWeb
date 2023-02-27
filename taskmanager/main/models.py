from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Назва', max_length=100)
    task = models.TextField('Завдання')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Всі завдання'
