# Generated by Django 5.1.1 on 2024-09-24 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='geolocation',
        ),
    ]
