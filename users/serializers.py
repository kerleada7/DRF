from rest_framework.serializers import HyperlinkedModelSerializer

from .models import UserCustom, Project, Todo


class UsersModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserCustom
        fields = ('username', 'first_name', 'last_name', 'email')


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'