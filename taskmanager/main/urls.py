from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('new_task',views.add_task, name='add_task'),
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),
    path('edit_task',views.edit_task, name='edit_task'),
    path('task_in_list', views.view_tasks, name='task_in_list'),
    path('new_tasklist', views.add_tasklist, name = 'add_tasklist'),
    path('tasklist_option', views.tasklist_options, name = 'tasklist_option')
]