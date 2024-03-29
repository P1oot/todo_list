from django.urls import path
from . import views

app_name = 'list'

urlpatterns = [
    path('', views.index, name='index'),
    path('deadline/', views.index_deadline, name='index_deadline'),
    path('task_create/', views.task_create, name='task_create'),
    path('group_create/', views.group_create, name='group_create'),
    path('group/<int:group_id>/', views.group_tasks, name='group_tasks'),
    path('task/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('group/<int:group_id>/edit/', views.group_edit, name='group_edit'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('group/<int:group_id>/delete/',
         views.group_delete, name='group_delete'),
]
