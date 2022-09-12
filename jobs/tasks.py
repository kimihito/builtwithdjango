from django.core.mail import send_mail


def notify_of_new_job(instance):
    message = f"""
      Someone submitted a new job.
      Instance: {instance}
    """
    send_mail(
        "New Job Submission",
        message,
        "rasul@builtwithdjango.com",
        ["rasul@builtwithdjango.com"],
        fail_silently=False,
    )
