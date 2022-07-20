from rest_framework import viewsets
from admin_panel.models import Category, Highlights, CustomUser
from admin_panel.api.serializers import CategorySerializer, HighlightsSerializer, UserSerializer, UserRegisterSerializer
from admin_panel.api.permissions import AnonPermissionOnly
from rest_framework import generics, permissions, views
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import generics, permissions, views
from rest_framework.response import Response
from rest_framework_jwt import settings

jwt_payload_handler             = settings.api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = settings.api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler    = settings.api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class HighlightsViewSet(viewsets.ModelViewSet):
    queryset = Highlights.objects.all()
    serializer_class = HighlightsSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class AuthAPIView(views.APIView):
    permission_classes = (AnonPermissionOnly,)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}, status=400)
        data = request.data
        phone_number = data.get('phone_number')
        password = data.get('password')
        qs = CustomUser.objects.filter(
                Q(phone_number__iexact=phone_number)|
                Q(email__iexact=phone_number)
            ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                print(user)
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token=token, user=user, request=request)
                return Response(response)
        return Response({"detail": "Invalid credentials"}, status=401)


class RegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AnonPermissionOnly]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get_serializer_context(self):
        return {'request': self.request}