# Generated by Django 3.2.15 on 2022-08-28 00:45

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_customuser_subscription_level"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaddleWebhook",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("payload", models.JSONField(default=None, null=True)),
            ],
        ),
        migrations.AddIndex(
            model_name="paddlewebhook",
            index=models.Index(fields=["created"], name="users_paddl_created_3439b5_idx"),
        ),
    ]
