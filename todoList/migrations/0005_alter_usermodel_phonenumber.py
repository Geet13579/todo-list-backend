# Generated by Django 5.0.1 on 2024-01-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0004_usermodel_phonenumber_usermodel_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='phoneNumber',
            field=models.CharField(max_length=10),
        ),
    ]
