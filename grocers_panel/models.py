from django.db import models

from admin_panel.models import CustomUser, StripeSubscription


class Grocer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    stripe_subscription = models.ForeignKey(StripeSubscription, on_delete=models.SET_NULL, null=True)
