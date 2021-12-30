from django.db.models import fields
from rest_framework import serializers
from admin_panel.models import Category, Highlights
from grocers_panel.models import Shop


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['title', 'img', 'count']

    def get_count(self, obj):
        return len(Shop.objects.all())


class HighlightsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Highlights
        fields = ['title', 'img']
