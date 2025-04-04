from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Category
from apps.grocers_panel.models import Grocer
from apps.buyers_panel.models import Buyer


class GrocerInline(admin.TabularInline):
    model = Grocer
    can_delete = False


class BuyerInline(admin.TabularInline):
    model = Buyer
    can_delete = False


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active', 'user_type',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'phone_number', 'is_phone_veryfied', 'date_joined')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'user_type')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2', 'is_staff', 'is_active', 'user_type', 'date_joined', 'is_phone_veryfied')},
         ),
    )
    search_fields = ('email', 'phone_number', 'last_name', 'first_name')
    ordering = ('email',)
    inlines = (GrocerInline, BuyerInline,)

    def get_inline_instances(self, request, obj=None):
        # Return no inlines when obj is being created
        if not obj:
            return []
        unfiltered = super(CustomUserAdmin, self).get_inline_instances(request, obj)
        # filter out the Inlines you don't want
        if obj.user_type == 'grocer':
            return [x for x in unfiltered if isinstance(x,GrocerInline)]
        else :
            return [x for x in unfiltered if isinstance(x,BuyerInline)]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'id', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)

class HighlightsAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'id', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
