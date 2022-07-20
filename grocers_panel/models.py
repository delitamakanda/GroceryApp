from taggit.managers import TaggableManager
from multiselectfield import MultiSelectField
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from admin_panel.models import CustomUser

CATEGORY_CHOICES = (
    ('TR', 'Trier'),
    ('OF', 'Offres'),
    ('DI', 'Diététique')
)

LABEL_CHOICES = (
    ('T', 'Toutes les offres'),
    ('J', 'Jusqu\'à 50% de réduction'),
    ('C', 'Choix de restaurants'),
    ('P', 'Commandez plus, économisez plus'),
    ('A', 'Articles gratuits'),
    ('M', 'Meals Deals')
)


class Grocer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Meal(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    info = models.CharField(max_length=255)
    discount_price = models.FloatField(blank=True, null=True)
    category = MultiSelectField(choices=CATEGORY_CHOICES, default='TR')
    label = MultiSelectField(choices=LABEL_CHOICES, default='T')
    stock_no = models.CharField(max_length=10, default=99)
    img = models.ImageField(upload_to='meal/%Y/%m/%d', blank=True)
    grocer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Meals'
        verbose_name = 'Meal'


class FoodMeal(models.Model):
    category = models.CharField(max_length=255)
    meals = models.ManyToManyField(Meal)
    grocer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Foods'
        verbose_name = 'Food'


class Shop(models.Model):
    SHORT = 1
    MEDIUM = 2
    LONG = 3
    VERY_LONG = 4
    DURATION_CHOICES = (
        (SHORT, '10 - 15'),
        (MEDIUM, '20 - 25'),
        (LONG, '35 - 45'),
        (VERY_LONG, '55 - 65'),
    )
    name = models.CharField(max_length=255)
    grocer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    # rating = models.ManyToManyField(CustomUser, through=Rating)
    # ratings = models.IntegerField(default=0)
    img = models.ImageField(upload_to='shop/%Y/%m/%d', blank=True)
    distance = models.FloatField()
    tags = TaggableManager()
    about = models.TextField(max_length=1000)
    duration = models.PositiveSmallIntegerField(
        default=LONG, choices=DURATION_CHOICES)
    food = models.ManyToManyField(FoodMeal)

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
        return str(self.rate)

# queryset be like shop.rating_set.all()
