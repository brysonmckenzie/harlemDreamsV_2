# Generated by Django 3.0.7 on 2020-07-28 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_app', '0020_auto_20200728_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='main_videoID_YouTube',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]