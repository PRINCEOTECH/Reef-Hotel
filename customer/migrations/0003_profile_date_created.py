# Generated by Django 4.1 on 2022-10-07 05:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]