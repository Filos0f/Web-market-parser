
# coding: utf-8

from django.conf.urls import url
from . import views
from . import parse_main

urlpatterns = [

	#url главной страницы
    url(r'^$', views.Main),
	
	#url общего парсинга
	url(r'^__parse/$', parse_main.ParserMain),
	
	#url товаров
	url(r'^(?P<sObject>[-\w]+)/$', views.Output)
]