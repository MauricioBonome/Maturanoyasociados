# Generated by Django 4.2.1 on 2023-05-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0003_property_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='vendido',
            field=models.BooleanField(default=False),
        ),
    ]
