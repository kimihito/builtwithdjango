# Generated by Django 3.0 on 2019-12-11 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_project_website_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
