# Generated by Django 3.2.3 on 2022-07-20 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocers_panel', '0016_rename_food_foodmeal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocer',
            name='stripe_subscription',
        ),
    ]
