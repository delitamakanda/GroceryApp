import uuid
from django.db import models


class Food(models.Model):
    POPULAR = 1
    RECOMMENDED = 2
    CATEGORY_CHOICES = (
        (POPULAR, 'popular'),
        (RECOMMENDED, 'recommended'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES, default=RECOMMENDED)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stars = models.IntegerField(default=0)
    img = models.ImageField(upload_to='food/%Y/%m/%d', blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at',]
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'
