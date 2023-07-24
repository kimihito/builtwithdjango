import logging

import requests
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.mail import send_mail

from .models import Project

logger = logging.getLogger(__file__)


def save_screenshot(project_title):
    project = Project.objects.get(title=project_title)

    image_url = (
        f"https://api.screenshotmachine.com?key={settings.SCREENSHOT_API_KEY}&url={project.url}&dimension=1680x876"
    )
    response = requests.get(image_url)

    logger.info(f"Getting info from {image_url}.")

    if response.status_code == 200:
        file = ContentFile(response.content)
    else:
        print(f"Error: {response.status_code} - {response.text}")

    project.homepage_screenshot.save(f"{project.title}.png", file, save=True)
    project.published = True
    project.save()


def notify_of_new_project(instance):
    message = f"""
      {instance.logged_in_maker} submitted a project ({instance.title} - {instance.url}).
    """
    send_mail(
        "New Project Submission",
        message,
        "Built with Django <rasul@builtwithdjango.com>",
        ["Built with Django <rasul@builtwithdjango.com>"],
        fail_silently=False,
    )


def notify_owner_of_new_comment(instance):
    try:
        project_instance = Project.objects.get(title=instance.project.title)
        project_owner_email = project_instance.logged_in_maker.email
    except AttributeError:
        project_owner_email = "Built with Django <rasul@builtwithdjango.com>"

    message = f"""
      {instance.author} left a comment on your project ({instance.project.url} - {instance.project}).
      Comment: {instance.comment}
    """

    send_mail(
        "New Comment on your Project",
        message,
        "Built with Django <rasul@builtwithdjango.com>",
        [project_owner_email],
        fail_silently=False,
    )


def notify_admins_of_comment(instance):
    message = f"""
      {instance.author} left a comment on project {instance.project.title} - {instance.project.url}.
      Comment: {instance.comment}
    """

    send_mail(
        f"New Comment on project {instance.project.title}",
        message,
        "Built with Django <rasul@builtwithdjango.com>",
        ["Built with Django <rasul@builtwithdjango.com>"],
        fail_silently=False,
    )
