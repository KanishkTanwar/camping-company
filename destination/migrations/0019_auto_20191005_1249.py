# Generated by Django 2.2.1 on 2019-10-05 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0018_auto_20191005_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='days',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
