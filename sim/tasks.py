#coding:utf-8
from celery import shared_task

from django_celery_simple_demo.celeryapp import debug_task


@shared_task
def task_add(x, y):
    result= x + y
    debug_task.delay('add result:{0}+{1}={2}'.format(x,y,result))
    return result


