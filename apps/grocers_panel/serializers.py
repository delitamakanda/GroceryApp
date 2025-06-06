from django.db.models import Avg, Count
from rest_framework import serializers
from taggit.models import Tag
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from apps.admin_panel.serializers import UserSerializer
from apps.grocers_panel.models import Meal, Grocer, FoodMeal, Shop, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['rate', 'shop', 'user']


class GrocerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Grocer
        fields = ['user',]


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'name', 'img', 'price', 'info', 'discount_price', 'category', 'label', 'stock_no', 'is_active']


class FoodSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)

    class Meta:
        model = FoodMeal
        fields = ['category', 'meals']


class OfferSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['name', 'count']

    def get_count(self, obj):
        shops = Shop.objects.filter(tags=obj)
        tags = Shop.tags.filter(shop__in=shops)
        tags = tags.annotate(tag_count=Count('taggit_taggeditem_items'))
        return len(tags)


class ShopSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    rating = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    food = FoodSerializer(many=True)
    grocer = UserSerializer()

    class Meta:
        model = Shop
        fields = ['id', 'grocer', 'name', 'rating', 'ratings', 'img',
                  'distance', 'img', 'tags', 'about', 'duration', 'food']

    def get_rating(self, obj):
        rating_average = list(
            obj.rating_set.aggregate(Avg('rate')).values())[0]
        return rating_average

    def get_ratings(self, obj):
        return len(obj.rating_set.all())

    def get_duration(self, obj):
        return obj.get_duration_display()
