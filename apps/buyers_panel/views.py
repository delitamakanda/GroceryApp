import requests
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.buyers_panel.serializers import OrderSerializer, BillingAddressSerializer, OrderItemSerializer
from apps.buyers_panel.models import Order, BillingAddress
from core.utils import IsOwnerOrReadOnly
from django.conf import settings


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

@api_view(['GET'])
def geocode(request):
    lat = request.query_params.get('lat', None)
    lng = request.query_params.get('lng', None)
    api_key = settings.GOOGLE_MAPS_API_KEY

    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}'.format(lat, lng, api_key))

    return Response(response.json(), status=status.HTTP_200_OK)

@api_view(['GET'])
def get_zone(request):
    lat = request.query_params.get('lat', None)
    lng = request.query_params.get('lng', None)
    api_key = settings.GOOGLE_MAPS_API_KEY
    # todo: get zone from lat and lng
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}'.format(lat, lng, api_key))

    return Response(response.json(), status=status.HTTP_200_OK)