from django.contrib.auth.models import AbstractUser
from django.db import models


class UserCustom(AbstractUser):
    email = models.EmailField(unique=True)


class Project(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField(blank=True)
    users = models.ManyToManyField(UserCustom)

    def __str__(self):
        return f'Проект {self.name}'


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(UserCustom, on_delete=models.CASCADE)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Проект: {self.project} ({self.user})'