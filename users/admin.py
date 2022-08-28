from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, PaddleWebhook


class CustomUserAdmin(UserAdmin):
    list_display = ["date_joined", "username", "email", "first_name", "last_name"]
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        (
            "Extra Fields",
            {
                "fields": (
                    "profile_image",
                    "subscription_level",
                    "referred_by",
                    "slug",
                    "make_public",
                    "twitter_handle",
                    "github_handle",
                    "indiehackers_handle",
                    "personal_website",
                    "interviewed",
                    "short_bio",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)


class PaddleWebhookAdmin(admin.ModelAdmin):
    list_display = [
        "created",
        "alert_name",
        "payload",
    ]
    model = PaddleWebhook


admin.site.register(PaddleWebhook, PaddleWebhookAdmin)
