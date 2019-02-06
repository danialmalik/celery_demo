from django.shortcuts import render
from celery.utils.log import get_task_logger

from .tasks import test_celery


logger = get_task_logger(__name__)


def index(request):
    value = test_celery.delay('debugging message')
    #logger.info('response from celery : {}'.format(value))
    return render(
        request,'index.html',
        {'response_text': 'celery task recieved. View logs to check status'}
    )
