from rest_framework import serializers
from admin_panel.models import Category, Highlights


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['title', 'img']


class HighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlights
        fields = ['title', 'img']
