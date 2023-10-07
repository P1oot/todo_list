from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()


class Group(models.Model):
    title = models.TextField(
        max_length=100,
        verbose_name='Название группы',
        help_text='Название группы',
    )
    description = models.TextField(
        verbose_name='Описание группы',
        help_text='Описание группы',
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group',
        verbose_name='User',
    )

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    title = models.TextField(
        max_length=70,
        verbose_name='Загодовок задачи',
        help_text='Задача',
    )
    description = models.TextField(
        verbose_name='Описание задачи',
        help_text='Описание',
        blank=True,
        null=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='todo_group',
        verbose_name='Группа',
        help_text='Группировка',
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='todo',
        verbose_name='User',
    )
    deadline = models.DateTimeField(
        verbose_name='Дедлайн',
        help_text='Дедлайн',
        default=datetime.now()
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        help_text='Дата создания',
        default=datetime.now()
    )
    # preority = models.IntegerField(
    #     verbose_name='Преоритет'
    # )

    def __str__(self) -> str:
        return self.title
