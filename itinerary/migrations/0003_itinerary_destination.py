# Generated by Django 2.2.1 on 2019-07-31 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0006_auto_20190731_1304'),
        ('itinerary', '0002_remove_itinerary_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='destination',
            field=models.ManyToManyField(blank=True, related_name='trips', to='destination.Destination'),
        ),
    ]
