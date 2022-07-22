from django.contrib import admin
from buyers_panel.models import BillingAddress, Order


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['id','user', 'shipping_address', 'ordered_date',]
    search_fields = ['ref_code',]
    ordering = ('ordered_date',)

class BillingAddressAdmin(admin.ModelAdmin):
    model = BillingAddress
    list_display = ['id', 'user', 'street_address', 'city', 'country',]
    search_fields = [ 'street_address', 'city', 'country',]
    ordering = ('address_type',)

admin.site.register(Order, OrderAdmin)
admin.site.register(BillingAddress, BillingAddressAdmin)