from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Category, Highlights
from grocers_panel.models import Grocer
from delivery_panel.models import Deliverer
from buyers_panel.models import Buyer


class GrocerInline(admin.TabularInline):
    model = Grocer
    can_delete = False


class DelivererInline(admin.TabularInline):
    model = Deliverer
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
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'user_type')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'user_type')},
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    inlines = (GrocerInline, BuyerInline, DelivererInline,)

    def get_inline_instances(self, request, obj=None):
        # Return no inlines when obj is being created
        if not obj:
            return []
        unfiltered = super(CustomUserAdmin, self).get_inline_instances(request, obj)
        # filter out the Inlines you don't want
        if obj.user_type == 'grocer':
            return [x for x in unfiltered if isinstance(x,GrocerInline)]
        elif obj.user_type == 'deliverer':
            return [x for x in unfiltered if isinstance(x,DelivererInline)]
        else :
            return [x for x in unfiltered if isinstance(x,BuyerInline)]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Highlights)
