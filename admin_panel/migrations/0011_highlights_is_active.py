# Generated by Django 3.2.3 on 2023-07-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0010_highlights_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlights',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]