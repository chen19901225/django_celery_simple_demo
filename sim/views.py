from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_celery_simple_demo.celeryapp import debug_task
from sim.tasks import task_add


def add(request, add1, add2):
    task_add.delay(int(add1), int(add2))
    debug_task.delay('execute add')
    return HttpResponse('Ok')
