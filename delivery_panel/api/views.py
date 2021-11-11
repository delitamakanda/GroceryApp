from rest_framework import viewsets
from admin_panel.models import CustomUser
from delivery_panel.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
