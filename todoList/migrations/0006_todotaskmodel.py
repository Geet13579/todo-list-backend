# Generated by Django 5.0.1 on 2024-01-21 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0005_alter_usermodel_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('status', models.TextField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]