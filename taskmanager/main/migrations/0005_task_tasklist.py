# Generated by Django 4.1.7 on 2023-02-28 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_tasklist_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='tasklist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.tasklist'),
        ),
    ]
