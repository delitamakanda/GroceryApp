from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.admin_panel.models import CustomUser
from apps.grocers_panel.models import Grocer


@post_save(sender=CustomUser, signal=post_save)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Grocer.objects.create(user=instance)
