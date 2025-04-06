from rest_framework import viewsets, status
from rest_framework.response import Response
from taggit.models import Tag
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from apps.grocers_panel.models import Grocer, Rating, Shop, Meal
from apps.grocers_panel.serializers import GrocerSerializer, ShopSerializer, RatingSerializer, OfferSerializer, MealSerializer
from apps.grocers_panel.services import GroceryService, MealService

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    service = MealService()
    
    def list(self, request):
        meals = self.service.get_queryset()
        serializer = self.serializer_class(meals, many=True)
        return Response(serializer.data)


class GrocerViewSet(viewsets.ModelViewSet):
    queryset = Grocer.objects.all()
    serializer_class = GrocerSerializer
    service = GroceryService()
    
    def list(self, request):
        grocers = self.service.get_queryset()
        serializer = self.serializer_class(grocers, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        grocer = self.service.get_by_id(pk)
        if grocer:
            serializer = self.serializer_class(grocer)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            grocer = self.service.create(**serializer.validated_data)
            return Response(self.serializer_class(grocer).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data, partial=True)
        if serializer.is_valid():
            grocer = self.service.update(pk, **serializer.validated_data)
            if grocer:
                return Response(self.serializer_class(grocer).data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        if self.service.delete(pk):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
        


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['tags__name', 'distance', 'food__meals__category', 'food__meals__label']
    search_fields = ['^name', '^about', '^food__category', '^food__meals__name', '^tags__name']


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()[:10]
    serializer_class = OfferSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['shop__id', 'user']
