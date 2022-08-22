from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()


class Group(models.Model):
    title = models.TextField(
        max_length=100,
        verbose_name='Название группы',
        help_text='Группировка задач',
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
        help_text='Описание задачи',
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
    created = models.DateTimeField(
        verbose_name='Запланированная дата',
        help_text='Запланированнвя дата',
        default=datetime.now()
        )

    def __str__(self) -> str:
        return self.title
