# Generated by Django 3.2.3 on 2023-07-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0009_auto_20230730_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlights',
            name='slug',
            field=models.SlugField(default='ee', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
