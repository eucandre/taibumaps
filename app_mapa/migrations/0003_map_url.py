# Generated by Django 4.2 on 2024-08-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mapa', '0002_map_farm'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
