from django.contrib import admin
from grocers_panel.models import Shop, Food, Meal, Rating


class MealAdmin(admin.ModelAdmin):
    model = Meal


class FoodAdmin(admin.ModelAdmin):
    model = Food


class ShopAdmin(admin.ModelAdmin):
    model = Shop
    list_display = ['name', 'tag_list']
    search_fields = ('name', 'id',)
    ordering = ('name',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Rating)
admin.site.register(Food, FoodAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Shop, ShopAdmin)
