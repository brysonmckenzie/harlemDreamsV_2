# Generated by Django 3.0.7 on 2020-07-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_app', '0023_auto_20200728_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camp',
            name='sign_up_deadline',
        ),
        migrations.AddField(
            model_name='camp',
            name='deadline',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='camp',
            name='details_list_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='camp',
            name='date_of_camp',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
