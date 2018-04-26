
# coding: utf-8

import pickle
from . import parsers

#чтобы добавить новый магазин, для него нужно сделать парсер товаров как сделано в файле parsers.py
#затем надо добавить информацию о магазине в словарь g_dictMarkets
#затем надо добавить для каждого товара url на страницу списка предложений этого магазина

#чтобы добавить товый товар нужно добавить словарь в g_dictObjects со строковым идентификатором этого товара (он же относительный url)
#затем добавить по аналогии информацию о товаре, а также url на списки предложений из доступных магазинов в g_dictMarkets

############################################################################

# список объектов парсинга
g_dictObjects = {
	
	#строковый идентификатор товара, он же /относительный_url/
	"videocards" : {
		
		#название которое будет показываться пользователю
		"text" : "Видеокарты",
		
		#url адреса для каждого магазина на страницу со списком предложений
		"urls" : {
			"DNS" : "https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/?stock=1",
			"Citilink" : "https://www.citilink.ru/catalog/computers_and_notebooks/parts/videocards/?action=changeCity&space=msk_cl:&available=1&status=55395790",
			"Ulmart" : "https://www.ulmart.ru/catalog/videocards"
		}
	},
	"ssd" : {
		"text" : "SSD накопители",
		"urls" : {
			"DNS" : "https://www.dns-shop.ru/catalog/8a9ddfba20724e77/ssd-nakopiteli/?stock=1",
			"Citilink" : "https://www.citilink.ru/catalog/computers_and_notebooks/hdd/ssd_in/?action=changeCity&space=msk_cl:&available=1&status=55395790",
			"Ulmart" : "https://www.ulmart.ru/catalog/hdd_ssd"
		}
	},
	"hdd_35" : {
		"text" : "Жесткие диски 3.5",
		"urls" : {
			"DNS" : "https://www.dns-shop.ru/catalog/17a8914916404e77/zhestkie-diski-35/?stock=1",
			"Citilink" : "https://www.citilink.ru/catalog/computers_and_notebooks/hdd/hdd_in/?action=changeCity&space=msk_cl:&available=1&status=55395790&p=1&f=211_32",
			"Ulmart" : "https://www.ulmart.ru/catalog/hdd_for_pc"
		}
	}
}

#список доступных магазинов
g_dictMarkets = {
	"DNS" : {
		"name" : "DNS",
		"link" : "https://www.dns-shop.ru/",
		"parser" : parsers.ParserDNS,
		},
	"Citilink" : {
		"name" : "Citilink",
		"link" : "https://www.citilink.ru/",
		"parser" : parsers.ParserCitilink,
		},
	"Ulmart" : {
		"name" : "Ulmart",
		"link" : "https://www.ulmart.ru/",
		"parser" : parsers.ParserUlmart,
		}
}

############################################################################

#запись сериализованных данных в файл
def Serialize(sPath, obj):
	with open(sPath, 'wb') as f:
		pickle.dump(obj, f)
	
#чтение сериализованных данных из файла
def Unserialize(sPath):
	with open(sPath, 'rb') as f:
		return pickle.load(f)