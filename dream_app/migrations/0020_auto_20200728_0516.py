# Generated by Django 3.0.7 on 2020-07-28 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_app', '0019_siteconfiguration_paypal_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camp',
            name='date',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='time',
        ),
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='paypal_link',
        ),
        migrations.AddField(
            model_name='camp',
            name='paypal_link',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
