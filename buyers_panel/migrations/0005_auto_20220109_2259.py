# Generated by Django 3.2.3 on 2022-01-09 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyers_panel', '0004_remove_buyer_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='billing_addresses',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_addresses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='buyers_panel.billingaddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='buyers_panel.billingaddress'),
        ),
    ]
