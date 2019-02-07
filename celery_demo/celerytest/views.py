from celery.utils.log import get_task_logger
from django.shortcuts import redirect, render

from .forms.email_form import EmailForm
from .tasks import task_send_email, task_test_celery

logger = get_task_logger(__name__)


def index(request):
    #value = test_celery.delay('debugging message')
    #logger.info('response from celery : {}'.format(value))
    email_form = EmailForm()
    return render(
        request, 'index.html',
        {
            'response_text': 'Enter ',
            'form': email_form
        }
    )


def send_email(request):
    if request.method == 'POST':
        reciever_address, email_content = request.POST['reciever_address'], request.POST['email_content']
        response = task_send_email.delay(reciever_address, email_content)
        logger.info('email task added to celery. [to: {}], [content: {}]'.format(
            reciever_address, email_content)
        )
        return redirect('/')
