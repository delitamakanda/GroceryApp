
import datetime
from admin_panel.api.serializers import UserSerializer
from django.utils import timezone

from rest_framework_jwt.settings import api_settings

expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA



def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data,
        'expires': timezone.now() + expire_delta - datetime.timedelta(seconds=200),
        'created_at': timezone.now(),
    }