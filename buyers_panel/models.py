from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from admin_panel.models import CustomUser
from grocery_api.models import Food
from django.core.validators import RegexValidator
from common.validators import phone_regex

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class BillingAddress(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    street_address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)
    contact_person_name = models.CharField(max_length=60, null=True, blank=True)
    contact_person_phone = models.CharField(max_length=60, validators=[phone_regex], null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Billing Addresses'
        verbose_name = 'Billing Address'

    def __str__(self):
        return self.street_address


class OrderItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=120)
    shipping_address = models.ForeignKey(
        BillingAddress, related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_addresses = models.ForeignKey(
        BillingAddress, related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField()
    ordered_date = models.DateTimeField(editable=False)
    ordered = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.user.first_name + ' ' + self.user.email

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.ordered_date = timezone.now()
        self.start_date = timezone.now()
        return super(Order, self).save(*args, **kwargs)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


class Buyer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
