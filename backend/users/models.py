from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Role(models.Model):
    rolename = models.CharField(max_length=100)
    permission = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
