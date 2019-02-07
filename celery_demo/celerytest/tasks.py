from celery.decorators import task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


@task(name='testing celery')
def task_test_celery(message):
    return 'Message recieved : {}'.format(message)


@task(name='send email')
def task_send_email(to_address, email_content):
    subject = 'celery test mail'
    from_address = settings.DEFAULT_FROM_EMAIL
    text_content = email_content
    html_content = get_template('emails/dummy_email.html').render({'email_content': email_content})
    msg = EmailMultiAlternatives(subject, text_content, from_address, [to_address])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
