# Generated by Django 3.0.5 on 2020-04-25 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20200425_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author_email',
        ),
        migrations.RemoveField(
            model_name='project',
            name='author_github',
        ),
        migrations.RemoveField(
            model_name='project',
            name='author_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='author_twitter',
        ),
        migrations.RemoveField(
            model_name='project',
            name='author_website',
        ),
    ]
