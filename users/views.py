from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import UserCustom
from .serializers import UsersModelSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UsersModelSerializer
