from django.forms import ModelForm
from .models import Task, Group


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'group', 'created')


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('title', 'description')
