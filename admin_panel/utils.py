import datetime
from admin_panel.api.serializers import UserSerializer
from django.utils import timezone


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data,
        'exp': datetime.timedelta(days=7),
        'created_at': timezone.now(),
    }