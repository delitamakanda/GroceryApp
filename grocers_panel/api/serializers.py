from django.db.models import Avg, Count
from rest_framework import serializers
from taggit.models import Tag
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from delivery_panel.api.serializers import UserSerializer
from grocers_panel.models import Meal, Grocer, Food, Shop, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['rate', 'shop', 'user']


class GrocerSerializer(serializers.ModelSerializer):
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


class OfferSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['name', 'count']

    def get_count(self, obj):
        shops = Shop.objects.filter(tags=obj)
        tags = Shop.tags.filter(shop__in=shops)
        tags = tags.annotate(tag_count=Count('taggit_taggeditem_items'))
        print(obj.__dict__)
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
