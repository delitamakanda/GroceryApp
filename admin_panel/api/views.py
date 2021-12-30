from rest_framework import viewsets
from admin_panel.models import Category, Highlights
from admin_panel.api.serializers import CategorySerializer, HighlightsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class HighlightsViewSet(viewsets.ModelViewSet):
    queryset = Highlights.objects.all()
    serializer_class = HighlightsSerializer
