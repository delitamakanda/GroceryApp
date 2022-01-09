from rest_framework import viewsets

from buyers_panel.api.serializers import OrderSerializer, BillingAddressSerializer
from buyers_panel.models import Order, BillingAddress


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BillingAddressViewSet(viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer
