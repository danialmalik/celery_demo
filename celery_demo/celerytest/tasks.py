from celery.decorators import task


@task(name="testing celery")
def test_celery(message):
    return "Message recieved : {}".format(message)
