from django.contrib import admin
from grocers_panel.models import Shop, FoodMeal, Meal, Rating, Grocer
from djangoql.admin import DjangoQLSearchMixin
from import_export.admin import ImportExportMixin

class MealAdmin(DjangoQLSearchMixin, ImportExportMixin, admin.ModelAdmin):
    model = Meal
    list_display = ['name', 'price']
    search_fields = ('name', 'id',)
    ordering = ('name',)
    list_filter = ('price',)



class FoodAdmin(admin.ModelAdmin):
    model = FoodMeal
    list_display = ['category', 'id']
    search_fields = ('category', 'id',)
    ordering = ('category',)
    filter_horizontal = ('meals',)



class ShopAdmin(admin.ModelAdmin):
    model = Shop
    list_display = ['name', 'tag_list']
    search_fields = ('name', 'id',)
    ordering = ('name',)
    filter_horizontal = ('tags',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Rating)
admin.site.register(FoodMeal, FoodAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Grocer)

