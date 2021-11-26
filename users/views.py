from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer

from .models import UserCustom, Project, Todo
from .serializers import UsersModelSerializer, ProjectModelSerializer, TodoModelSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UsersModelSerializer


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TodoModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
