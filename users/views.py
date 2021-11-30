from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer

from .models import UserCustom, Project, Todo
from .serializers import UsersModelSerializer, ProjectModelSerializer, TodoModelSerializer

from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class UsersLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoFilter(filters.FilterSet):
    create = filters.DateFromToRangeFilter(label='Дата создания в формате гггг-мм-дд')

    class Meta:
        model = Todo
        fields = ['project', 'create']


class UsersModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UsersModelSerializer
    pagination_class = UsersLimitOffsetPagination


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter


class TodoModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer

    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilter

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_200_OK)

