# Generated by Django 2.2.1 on 2019-08-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0011_remove_region_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='note',
            field=models.CharField(default='12', max_length=128),
            preserve_default=False,
        ),
    ]
