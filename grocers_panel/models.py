from django.db import models

from admin_panel.models import CustomUser


class Grocer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
