# Generated by Django 2.0.7 on 2019-01-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20190125_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='customer',
            name='nickname',
            field=models.CharField(max_length=64),
        ),
    ]
