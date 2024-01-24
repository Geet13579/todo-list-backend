from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class GeeksModel(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.title
from django.db import models


class GeeksModel(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.title
	

class UserModel(models.Model):
    username = models.CharField(max_length=200)
    email = models.TextField()
    password = models.TextField()
    token = models.TextField(null=True)

    def __str__(self):
        return self.username  # Use an appropriate field like 'username' here

class TodoTaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField()
    status = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.task
	

