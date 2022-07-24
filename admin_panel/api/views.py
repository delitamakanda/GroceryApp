from rest_framework import viewsets, request, status, generics, permissions, views
from admin_panel.models import Category, Highlights, CustomUser
from admin_panel.api.serializers import CategorySerializer, HighlightsSerializer, UserSerializer, UserRegisterSerializer
from admin_panel.api.permissions import AnonPermissionOnly
from django.contrib.auth import authenticate, get_user_model
from django.http import Http404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework_jwt import settings
from common.permissions import IsOwnerOrReadOnly

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
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'errors': 'You are already authenticated'}, status=400)
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
        return Response({"errors": "Invalid credentials"}, status=401)


class RegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AnonPermissionOnly]
    authentication_classes = []

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class UserDetailAPIView(views.APIView):
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated,]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data, status=200)

    def put(self, request, format=None):
        user_obj = self.get_object(request.user.id)
        serializer = UserSerializer(user_obj, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)