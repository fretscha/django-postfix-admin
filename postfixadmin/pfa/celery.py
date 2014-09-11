from future import absolute_import

import os
import django

from celery import Celery
from django.conf import settings

django.setup()

app = Celery('pfa')

app.config_from_object('django.conf:settings')
app.autodiscover(lambda: settings.INSTALLED_APPS)
