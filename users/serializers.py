from rest_framework.serializers import HyperlinkedModelSerializer

from .models import UserCustom


class UsersModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserCustom
        fields = ('username', 'first_name', 'last_name', 'email')