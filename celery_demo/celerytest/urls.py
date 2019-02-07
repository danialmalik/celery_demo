from django.conf.urls import url

from .views import index, send_email

app_name = 'celerytest'

urlpatterns = [
    url(r'^$', index, name='index_view'),
    url(r'^send_email/$', send_email, name='send_email_view')
]
