# Generated by Django 3.0.7 on 2020-07-28 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_app', '0021_siteconfiguration_main_videoid_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='main_videoID_YouTube',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]