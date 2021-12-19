from django.contrib import admin
from grocers_panel.models import Shop, Food, Meal, Rating


class MealAdmin(admin.ModelAdmin):
    model = Meal


class FoodAdmin(admin.ModelAdmin):
    model = Food


class ShopAdmin(admin.ModelAdmin):
    model = Shop


admin.site.register(Rating)
admin.site.register(Food, FoodAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Shop, ShopAdmin)
