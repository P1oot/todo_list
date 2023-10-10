from django.shortcuts import render, redirect, get_object_or_404
from .models import Group, Task
from .forms import TaskForm, GroupForm


def index_base(request, template, todo_list):
    user_is_auth = request.user.is_authenticated
    group_list = Group.objects.filter(author=request.user.id).all()
    context = {
        'is_auth': user_is_auth,
        'todo_list': todo_list,
        'group_list': group_list,
    }
    return context


def index(request):
    template = 'todo/index.html'
    todo_list = Task.objects.filter(author=request.user.id).all()
    context = index_base(request, template, todo_list)
    return render(request, template, context)


def index_deadline(request):
    template = 'todo/index.html'
    todo_list = (Task.objects.filter(author=request.user)
                 .order_by('-deadline').all())
    context = index_base(request, template, todo_list)
    context['is_deadline'] = True
    return render(request, template, context)


def group_tasks(request, group_id):
    template = 'todo/group_tasks.html'
    todo_list = Task.objects.filter(author=request.user, group=group_id).all()
    group = Group.objects.get(pk=group_id)
    context = {
        'todo_list': todo_list,
        'group': group,
    }
    return render(request, template, context)


def task_create(request):
    template = 'todo/creation.html'
    form = TaskForm(request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            print(request.user)
            form.save()
            return redirect('list:index')
    context = {
        'form': form,
    }
    return render(request, template, context)


def group_create(request):
    template = 'todo/creation.html'
    form = GroupForm(request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            form.save()
            return redirect('list:index')
    context = {
        'form': form,
        'is_group': True,
    }
    return render(request, template, context)


def task_edit(request, task_id):
    template = 'todo/creation.html'
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(
        request.POST or None,
        files=request.FILES or None,
        instance=task
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list:index')
    context = {
        'form': form,
        'task_id': task_id,
        'is_edit': True,
    }
    return render(request, template, context)


def group_edit(request, group_id):
    template = 'todo/creation.html'
    group = get_object_or_404(Group, id=group_id)
    form = GroupForm(
        request.POST or None,
        files=request.FILES or None,
        instance=group
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list:index')
    context = {
        'form': form,
        'group_id': group_id,
        'is_group': True,
        'is_edit': True,
    }
    return render(request, template, context)


def task_delete(request, task_id):
    Task.objects.filter(author=request.user, id=task_id).delete()
    return redirect('list:index')


def group_delete(request, group_id):
    Group.objects.filter(author=request.user, id=group_id).delete()
    return redirect('list:index')
