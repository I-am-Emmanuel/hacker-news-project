from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hacker_news.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1') # This line can be commented out if this code is running on a linux machine

celery = Celery('hacker_news')


celery.config_from_object("django.conf:settings", namespace='CELERY')


# celery.conf.beat_schedule = {
# 'create_custome_hackn': {
# 'task': 'news.tasks.create_custome_hackn',
# 'schedule': crontab(minute='*/5'),
#     },
# }

celery.conf.broker_connection_retry_on_startup = True

celery.autodiscover_tasks()


# @celery.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))




