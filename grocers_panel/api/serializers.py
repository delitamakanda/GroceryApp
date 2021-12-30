from django.db.models import fields
from rest_framework import serializers
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from grocers_panel.models import Meal, Grocer, Food, Shop, Rating


class GrocerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grocer
        fields = ['user', 'stripe_subscription']


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'name', 'img', 'price', 'info']


class FoodSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)
    class Meta:
        model = Food
        fields = ['category', 'meals']


class ShopSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    rating = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    food = FoodSerializer(many=True)

    class Meta:
        model = Shop
        fields = ['id', 'grocer', 'name', 'rating', 'ratings', 'img',
                  'distance', 'img', 'tags', 'about', 'duration', 'food']

    def get_rating(self, obj):
        return ''

    def get_duration(self, obj):
        return obj.get_duration_display()
