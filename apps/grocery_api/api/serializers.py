from rest_framework import serializers

from apps.grocery_api.models import Food

class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'
