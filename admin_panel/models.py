from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GROCER = 1
    BUYER = 2
    DELIVERER = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (GROCER, 'grocer'),
        (BUYER, 'buyer'),
        (DELIVERER, 'deliverer'),
        (ADMIN, 'admin'),
    )
    # username = None
    email = models.EmailField(_('Email'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, default=BUYER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email + ' ' + self.get_user_type_display()


class StripeSubscription(models.Model):
    start_date = models.DateTimeField()
    status = models.CharField(max_length=20)


class Category(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='category', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


class Highlights(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='highlights', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']
        verbose_name_plural = 'Highlights'
        verbose_name = 'Highlight'
