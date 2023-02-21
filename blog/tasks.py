from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_feedback(form):
    subject = f'Feedback from {form["name"]} | {form["email"]}'
    message = form['message']
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['6234513@gmail.com']
    )
