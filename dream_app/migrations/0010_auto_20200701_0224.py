# Generated by Django 3.0.7 on 2020-07-01 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dream_app', '0009_camp_mediaphoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='camp',
            old_name='info_2',
            new_name='detail_info',
        ),
        migrations.RenameField(
            model_name='camp',
            old_name='camp_title',
            new_name='title',
        ),
    ]