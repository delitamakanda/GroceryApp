# Generated by Django 4.2.20 on 2025-04-04 19:15

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('grocers_panel', '0017_remove_grocer_stripe_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('TR', 'Trier'), ('OF', 'Offres'), ('DI', 'Diététique')], default='TR', max_length=2),
        ),
        migrations.AlterField(
            model_name='meal',
            name='label',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('T', 'Toutes les offres'), ('J', "Jusqu'à 50% de réduction"), ('C', 'Choix de restaurants'), ('P', 'Commandez plus, économisez plus'), ('A', 'Articles gratuits'), ('M', 'Meals Deals')], default='T', max_length=1),
        ),
    ]
