# Generated by Django 2.2.28 on 2022-08-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_task_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(help_text='Запланированнвя дата', verbose_name='Запланированная дата'),
        ),
    ]