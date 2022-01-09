# Generated by Django 3.2.3 on 2022-01-09 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocers_panel', '0013_remove_shop_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='category',
            field=models.CharField(choices=[('TR', 'Trier'), ('OF', 'Offres'), ('DI', 'Diététique')], default='TR', max_length=2),
        ),
        migrations.AddField(
            model_name='meal',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='label',
            field=models.CharField(choices=[('T', 'Toutes les offres'), ('J', "Jusqu'à 50% de réduction"), ('C', 'Choix de restaurants'), ('P', 'Commandez plus, économisez plus'), ('A', 'Articles gratuits'), ('M', 'Meals Deals')], default='T', max_length=1),
        ),
        migrations.AddField(
            model_name='meal',
            name='stock_no',
            field=models.CharField(default=99, max_length=10),
        ),
    ]
