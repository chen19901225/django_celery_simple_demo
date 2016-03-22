# coding:utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/(?P<add1>\d+)/(?P<add2>\d+)/?$', views.add)
]
