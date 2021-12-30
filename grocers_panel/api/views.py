from rest_framework import viewsets
from grocers_panel.models import Grocer, Shop
from grocers_panel.api.serializers import GrocerSerializer, ShopSerializer


class GrocerViewSet(viewsets.ModelViewSet):
    queryset = Grocer.objects.all()
    serializer_class = GrocerSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
