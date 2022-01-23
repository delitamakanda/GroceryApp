from rest_framework import viewsets

from buyers_panel.api.serializers import OrderSerializer, BillingAddressSerializer
from buyers_panel.models import Order, BillingAddress


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BillingAddressViewSet(viewsets.ModelViewSet):
    serializer_class = BillingAddressSerializer
    queryset = BillingAddress.objects.all()

    def get_queryset(self):
        billing_addresses = BillingAddress.objects.filter(user=self.request.user)
        return billing_addresses
