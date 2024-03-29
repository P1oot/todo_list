# Generated by Django 2.2.28 on 2022-08-22 22:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 23, 1, 15, 16, 695106), help_text='Запланированнвя дата', verbose_name='Запланированная дата'),
        ),
        migrations.AlterField(
            model_name='task',
            name='group',
            field=models.ForeignKey(blank=True, help_text='Группировка', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todo_group', to='list.Group', verbose_name='Группа'),
        ),
    ]
