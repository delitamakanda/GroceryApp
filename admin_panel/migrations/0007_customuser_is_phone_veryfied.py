# Generated by Django 3.2.3 on 2022-07-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_auto_20220720_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_phone_veryfied',
            field=models.BooleanField(default=False),
        ),
    ]
