from rest_framework import serializers

from apps.buyers_panel.models import BillingAddress, Order, OrderItem
from apps.food_panel.serializers import FoodSerializer


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        exclude = ['created_at', 'updated_at',]


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
