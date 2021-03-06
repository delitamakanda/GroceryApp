# Generated by Django 3.2.3 on 2022-07-22 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_api', '0001_initial'),
        ('buyers_panel', '0005_auto_20220109_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='billingaddress',
            options={'verbose_name': 'Billing Address', 'verbose_name_plural': 'Billing Addresses'},
        ),
        migrations.RemoveField(
            model_name='billingaddress',
            name='apartment_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='coupon',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery_api.food'),
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
