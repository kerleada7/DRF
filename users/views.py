from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer

from .models import UserCustom
from .serializers import UsersModelSerializer

from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class UsersLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5



class UsersModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UsersModelSerializer
    pagination_class = UsersLimitOffsetPagination
