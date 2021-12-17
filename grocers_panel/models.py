from taggit.managers import TaggableManager
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from admin_panel.models import CustomUser, StripeSubscription


class Grocer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    stripe_subscription = models.ForeignKey(
        StripeSubscription, on_delete=models.SET_NULL, null=True)


class Meal(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    info = models.CharField(max_length=255)
    img = models.ImageField(upload_to='meal/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Meals'
        verbose_name = 'Meal'


class Food(models.Model):
    category = models.CharField(max_length=255)
    meals = models.ForeignKey(Meal, on_delete=models.CASCADE)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Foods'
        verbose_name = 'Food'


class Shop(models.Model):
    name = models.CharField(max_length=255)
    # rating = models.ManyToManyField(CustomUser, through=Rating)
    ratings = models.IntegerField(blank=True)
    img = models.ImageField(upload_to='shop/%Y/%m/%d', blank=True)
    distance = models.FloatField()
    tags = TaggableManager()
    about = models.TextField(max_length=1000)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Shops'
        verbose_name = 'Shop'


class Rating(models.Model):
    rate = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.rate

# queryset be like shop.rating_set.all()
