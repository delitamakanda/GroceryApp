from rest_framework import viewsets
from taggit.models import Tag
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from grocers_panel.models import Grocer, Rating, Shop
from grocers_panel.api.serializers import GrocerSerializer, ShopSerializer, RatingSerializer, OfferSerializer


class GrocerViewSet(viewsets.ModelViewSet):
    queryset = Grocer.objects.all()
    serializer_class = GrocerSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['tags__name']
    search_fields = ['^name', 'about', '^food__meals__name']


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()[:10]
    serializer_class = OfferSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['shop__id', 'user']
