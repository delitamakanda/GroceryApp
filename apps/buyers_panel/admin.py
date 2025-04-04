from django.contrib import admin
from apps.buyers_panel.models import BillingAddress, Order, OrderItem, Refund, Buyer
from import_export.admin import ImportExportMixin
from django.urls import reverse
from django.utils.html import format_html

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

class OrderAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Order
    list_display = ['id', 'link_to_customer', 'shipping_address', 'ordered_date', 'status',]
    search_fields = ['ref_code', 'user__email',]
    ordering = ('ordered_date',)
    filter_horizontal = ('items',)
    list_filter = ('status', OnlyActiveOrdersFilter, 'ordered', 'being_delivered', 'received',)
    list_display_links = ('id', 'ordered_date',)
    list_select_related = ('user',)

    def link_to_customer(self, obj):
        link = reverse('admin:admin_panel_customuser_change', args=[obj.user.id])
        return format_html('<a href="{}">{}</a>', link, obj.user)
    link_to_customer.short_description = 'Customer'

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
