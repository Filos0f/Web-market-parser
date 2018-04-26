
# coding: utf-8

from django.http import HttpResponse
from .models import Product
from . import parsers
from . import g_data

############################################################################

#обработчик для сортировки
def sortByCost(key):
	return key["cost"]

#функция запускаящая парсинг в соответсвии с товарами в g_dictObjects и магазинами в g_dictMarkets
def ParserMain(request):
	listFromMarkets = []
	dictFromMarkets = {}
	
	for sNameObj in g_data.g_dictObjects:
		listFromMarkets.append([])
		dictFromMarkets[sNameObj] = []
		iCurrNum = 0
		for sNameMarket in g_data.g_dictMarkets:
			listMarketProducts = g_data.g_dictMarkets[sNameMarket]["parser"](g_data.g_dictObjects[sNameObj]["urls"][sNameMarket])
			listFromMarkets[iCurrNum].append(listMarketProducts)
			dictFromMarkets[sNameObj].extend(listMarketProducts)
		iCurrNum += 1
		dictFromMarkets[sNameObj].sort(key=sortByCost)
		g_data.Serialize("serialize_" + sNameObj + ".txt", dictFromMarkets[sNameObj])
		
	if len(dictFromMarkets) > 0:
		Product.objects.all().delete()
	else:
		return HttpResponse("none products :(")
		
	for sNameObj in dictFromMarkets:
		for obj in dictFromMarkets[sNameObj]:
			if obj['img'] == None:
				obj['img'] = "";
			new_product = Product.objects.create(name=obj['name'], desc=obj['desc'], type=sNameObj, cost=obj['cost'], img=obj['img'], link=obj['link'], market=obj['market']);
			new_product.save();
			
	return HttpResponse("ok :)")