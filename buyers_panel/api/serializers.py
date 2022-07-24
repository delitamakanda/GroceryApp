from rest_framework import serializers

from buyers_panel.models import BillingAddress, Order, OrderItem
from grocery_api.api.serializers import FoodSerializer


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    item = FoodSerializer(read_only=True)

    class Meta:
        model = OrderItem
        exclude = ('user',)


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        exclude = ('user',)
