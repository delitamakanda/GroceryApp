from django.contrib import admin
from buyers_panel.models import BillingAddress, Order, OrderItem, Refund, Buyer

class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ['user', 'item', 'quantity',]


class OnlyActiveOrdersFilter(admin.SimpleListFilter):
    title = 'Show only active orders'
    parameter_name = 'status'
    def lookups(self, request, model_admin):
        return (
            ('active', 'Active'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'active':
            return queryset.filter(status__in=('P', 'O'))
        return queryset

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['id','user', 'shipping_address', 'ordered_date', 'status']
    search_fields = ['ref_code', 'user',]
    ordering = ('ordered_date',)
    filter_horizontal = ('items',)
    list_filter = ('status', OnlyActiveOrdersFilter, 'ordered', 'being_delivered', 'received',)

class BillingAddressAdmin(admin.ModelAdmin):
    model = BillingAddress
    list_display = ['id', 'user', 'street_address', 'city', 'country', 'address_type']
    search_fields = [ 'street_address', 'city', 'country',]
    ordering = ('address_type',)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(BillingAddress, BillingAddressAdmin)
admin.site.register(Refund)
admin.site.register(Buyer)
