# Generated by Django 3.2.13 on 2022-07-10 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="project",
            new_name="post",
        ),
    ]
