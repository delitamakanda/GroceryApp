from django.contrib import admin
from .models import Food


class FoodAdmin(admin.ModelAdmin):
    model = Food
    list_display = ['name', 'created_at', 'category',]
    search_fields = ['name', 'id', 'description',]
    ordering = ('created_at',)

admin.site.register(Food, FoodAdmin)
