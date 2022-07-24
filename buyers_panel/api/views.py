from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from buyers_panel.api.serializers import OrderSerializer, BillingAddressSerializer, OrderItemSerializer
from buyers_panel.models import Order, BillingAddress
from grocery_api.models import Food
from common.permissions import IsOwnerOrReadOnly


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated,]

    def get_queryset(self):
        orders_list = Order.objects.filter(user=self.request.user)
        return orders_list

    def create(self, request):
        order_item_serializer = OrderItemSerializer(data=request.data)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid() and order_item_serializer.is_valid():
            serializer.save(user=request.user)
            order_item_serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BillingAddressViewSet(viewsets.ModelViewSet):
    serializer_class = BillingAddressSerializer
    queryset = BillingAddress.objects.all()
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated,]

    def get_queryset(self):
        billing_addresses = BillingAddress.objects.filter(user=self.request.user)
        return billing_addresses

    def create(self, request):
        serializer = BillingAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
