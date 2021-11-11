from django.db import models

from django.db import models

from admin_panel.models import CustomUser


class Deliverer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
