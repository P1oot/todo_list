from django.urls import path
from . import views

app_name = 'list'

urlpatterns = [
    path('', views.index, name='index'),
    path('task_create/', views.task_create, name='task_create'),
    path('group_create/', views.group_create, name='group_create'),
    path('task/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('group/<int:group_id>/edit/', views.group_edit, name='group_edit')
]
