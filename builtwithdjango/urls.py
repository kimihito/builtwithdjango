"""builtwithdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


# Sitemap imports
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from .sitemaps import StaticViewSitemap

from projects.models import Project

sitemaps = {
    "static": StaticViewSitemap,
    "projects": GenericSitemap(
        {
            "queryset": Project.objects.filter(published=True),
            "date_field": "date_added",
        },
        priority=0.8,
    ),
}


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path(
            "sitemap.xml",
            sitemap,
            {"sitemaps": sitemaps},
            name="django.contrib.sitemaps.views.sitemap",
        ),
        path("", include("projects.urls")),
        path("newsletter/", include("newsletter.urls")),
        path("sentry-debug/", trigger_error),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns