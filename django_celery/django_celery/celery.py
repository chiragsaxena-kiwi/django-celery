
from __future__ import absolute_import, unicode_literals
from urllib.request import Request

from pytz import timezone

import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from django_celery_beat.models import PeriodicTask


os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery.settings')

app=Celery('django_celery')
app.conf.enable_utc=False

app.conf.update(timezone='Asia/Kolkata')


app.config_from_object(settings,namespace='CELERY')



#CELERY BEAT SETTINGS

app.conf.beat_schdule = {
    'send-mail-every-day-at-8': {
        'task':'send_mail_app.task.send_mail_func',
        'schdule':crontab(hour=12,minute=44),
       
    }
    
}

app.autodiscover_tasks()
@app.task(bind=True)

def debug_task(self):
    print(f,'Request: {self.request!r}')