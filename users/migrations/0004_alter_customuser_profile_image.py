# Generated by Django 3.2.11 on 2022-01-26 22:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_customuser_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_image",
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name="Image"),
        ),
    ]
