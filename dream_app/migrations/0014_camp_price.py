# Generated by Django 3.0.7 on 2020-07-22 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_app', '0013_auto_20200715_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
