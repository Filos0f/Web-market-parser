
# coding: utf-8

from django.shortcuts import render
import os
from . import g_data
from .models import Product
from django.db.models import Q
from django.http import HttpResponse

############################################################################

#вывод главной страницы, с таблицами по 5 самых дешевых предложенний
def Main(request):

	if request.method == "POST" and "text" in request.POST and request.POST["text"]:
		objs = Product.objects.filter(Q(name__icontains=request.POST["text"]))
			
		return render(request, 'index.html', {"g_dictObjects": g_data.g_dictObjects, "g_dictMarkets": g_data.g_dictMarkets, "title": "Поиск", "header": "Поиск [" + request.POST["text"] + "]", "listFound": objs, "lenObjects": str(len(objs))}, status=200)
	
	dictCheaps = {}
	
	for sObject in g_data.g_dictObjects:
		dictCheaps[sObject] = [g_data.g_dictObjects[sObject]["text"],[]]
		listObjects = Product.objects.filter(type=sObject).order_by("cost")[:5]
		for obj in listObjects:
			dictCheaps[sObject][1].append(obj)
	
	return render(request, 'index.html', {"g_dictObjects": g_data.g_dictObjects, "g_dictMarkets": g_data.g_dictMarkets, "title": "Главная","header": "Самые дешевые товары", "dictCheaps": dictCheaps}, status=200)

#вывод общего списка товаров (в виде таблицы)
def Output(request, sObject):

	if sObject in g_data.g_dictObjects:
		listObjects = Product.objects.filter(type=sObject)
		if len(listObjects) > 0:
			return render(request, 'index.html', {"g_dictObjects": g_data.g_dictObjects, "g_dictMarkets": g_data.g_dictMarkets, "title": g_data.g_dictObjects[sObject]["text"],"listObjects": listObjects, "min_cost": listObjects[0].cost, "max_cost": listObjects[len(listObjects) - 1].cost, "lenObjects": str(len(listObjects)), "header": g_data.g_dictObjects[sObject]["text"]}, status=200)
		else:
			return render(request, 'index.html', {"g_listObjects": g_data.g_dictObjects, "g_dictMarkets": g_data.g_dictMarkets, "title": "Данных еще нет, зайдите позже :)","header": "Данных еще нет, зайдите позже :)"}, status=200)
	else:
		return render(request, 'index.html', {"g_dictObjects": g_data.g_dictObjects, "g_dictMarkets": g_data.g_dictMarkets, "title": "404 | Такого товара нет в списке :)","header": "Такого товара нет в списке :("}, status=404)
		