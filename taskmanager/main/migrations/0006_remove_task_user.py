# Generated by Django 4.1.7 on 2023-02-28 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_task_tasklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]