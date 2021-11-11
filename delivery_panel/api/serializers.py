from rest_framework import serializers
from admin_panel.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'email', 'is_staff', 'user_type']
