# coding:utf-8

from celery import Celery

import os

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_simple_demo.settings')

app = Celery('django_celery_simple_demo')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=False)
def debug_task(info):
    print("Info {0}".format(info))
