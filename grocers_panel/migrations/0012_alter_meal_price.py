# Generated by Django 3.2.3 on 2021-12-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocers_panel', '0011_shop_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.FloatField(),
        ),
    ]
