# Generated by Django 5.0.1 on 2024-01-22 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0010_usermodel_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='last_login',
        ),
    ]