# Generated by Django 2.0.7 on 2019-05-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_auto_20190503_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='lead_status',
            field=models.CharField(blank=True, choices=[('Lead Closed', 'Lead Closed'), ('Follow Up', 'Follow Up')], max_length=128, null=True),
        ),
    ]
