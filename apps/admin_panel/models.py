from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils.text import slugify
from core.models import BaseModel

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GROCER = 1
    BUYER = 2
    ADMIN = 4
    ROLE_CHOICES = (
        (GROCER, 'grocer'),
        (BUYER, 'buyer'),
        (ADMIN, 'admin'),
    )
    phone_message = 'Phone number must be entered in the format: 05999999999' 

     # your desired format 
    phone_regex = RegexValidator(
        regex=r'^(\d{2})\d{8}$',
        message=phone_message
    )
    last_name = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150)
    email = models.EmailField(_('Email'), unique=True)
    phone_number = models.CharField(max_length=60, unique=True, validators=[phone_regex])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    mail_is_verified = models.BooleanField(default=False)
    is_phone_veryfied = models.BooleanField(default=False)
    user_type = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, default=BUYER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email + ' ' + self.get_user_type_display()


class Category(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    img = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
