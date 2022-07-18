from rest_framework import viewsets, response, permissions
from grocery_api.models import Food
from .serializers import FoodSerializer, FoodCreateSerializer
from grocery_api.pagination import LargeResultsSetPagination, StandardResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# get the integer value for the input string
value_map = {v: k for k, v in Food.CATEGORY_CHOICES}

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_classes = {
        'list': FoodSerializer,
        'retrieve': FoodSerializer
    }
    default_serializer_class = FoodCreateSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = [permissions.AllowAny,] #todo: remove
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = (
        'price',
    )
    search_fields = ['name', 'description',]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_object(self):
        return self.get_queryset()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return response.Response(serializers.data)


class PopularFoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.filter(category=value_map['popular'])[:10]  
    serializer_classes = {
        'list': FoodSerializer,
        'retrieve': FoodSerializer
    }
    default_serializer_class = FoodCreateSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [permissions.AllowAny,] #todo: remove
    ordering_fields = (
        'price',
    )
    search_fields = ['name', 'description',]
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class RecommendedFoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.filter(category=value_map['recommended'])[:10]
    serializer_classes = {
        'list': FoodSerializer,
        'retrieve': FoodSerializer
    }
    default_serializer_class = FoodCreateSerializer
    permission_classes = [permissions.AllowAny,] #todo: remove
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = (
        'price',
    )
    search_fields = ['name', 'description',]
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class DrinksViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.filter(category=value_map['drinks'])[:10]
    serializer_classes = {
        'list': FoodSerializer,
        'retrieve': FoodSerializer
    }
    default_serializer_class = FoodCreateSerializer
    permission_classes = [permissions.AllowAny,] #todo: remove
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = (
        'price',
    )
    search_fields = ['name', 'description',]
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
