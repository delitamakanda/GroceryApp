from rest_framework import serializers

from grocery_api.models import Food

class FoodSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex_verbose')

    class Meta:
        model = Food
        fields = '__all__'

class FoodCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'
