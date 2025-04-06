from rest_framework import serializers

from apps.food_panel.models import Food

class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'
