
# coding: utf-8

from grab import Grab
import bs4

############################################################################

#парсер товаров для магазина DNS
def ParserDNS(sLink):
	g = Grab()
	
	sPage = ""
	iPage = 1
	listProducts = []
	
	while 1:
		sCurrURL = sLink + "&p=" + str(iPage)
		sPage = g.go(sCurrURL, reuse_cookies=1, cookiefile="cookies.txt", connect_timeout=1000, timeout=3000).body
		print(str(g.response.code) + " -- " + sCurrURL + "\n")
		if g.response.code != 200:
			break
		
		bsoup = bs4.BeautifulSoup(sPage, "html.parser")
		divs = bsoup.findAll("div", class_="catalog-item-inner catalog-product view-list has-avails")
	
		for div in divs:
			dictProduct = {}
			div_product_info = div.find('div', {'class': 'product-info'})
			dictProduct["img"] = div_product_info.find('div', {'class': 'image'}).find("img")
			
			if dictProduct["img"].get("src"):
				dictProduct["img"] = dictProduct["img"].get("src")
			else:
				dictProduct["img"] = dictProduct["img"].get("data-src")
				
			dictProduct["link"] = "https://www.dns-shop.ru" + div_product_info.find('div', {'class': 'title'}).find("a").get("href")
			dictProduct["name"] = div_product_info.find('div', {'class': 'title'}).find("a").text
			dictProduct["desc"] = div_product_info.find('div', {'class': 'title'}).find("span").text
			dictProduct["cost"] = int(div.find('div', {'class': 'product-price'}).find('div', {'class': 'price_g'}).find('span').text.replace(' ', ''))
			dictProduct["market"] = "DNS";
			
			listProducts.append(dictProduct)
			
		iPage += 1
		
		oDisabledSpan = bsoup.find("span", class_="disabled item next")
		
		if oDisabledSpan:
			break
		
		#if iPage >= 10:
			#break
			
	return listProducts
	
############################################################################
	
#парсер товаров для магазина Citilink
def ParserCitilink(sLink):
	g = Grab()
	
	#html_str = ""
	sPage = ""
	iPage = 1
	listProducts = []
	
	while iPage > 0:
		sCurrURL = sLink + "&p=" + str(iPage) #+ "&sorting=price_asc"
		sPage = g.go(sCurrURL, reuse_cookies=1, cookiefile="cookies.txt", connect_timeout=1000, timeout=3000).body
		
		#f = open("_Citilink" + ".html", 'w')
		#f.write(str(sPage))
		#f.close()
		print(str(g.response.code) + " -- " + sCurrURL + "\n")
		
		if g.response.code != 200:
			break
		
		bsoup = bs4.BeautifulSoup(sPage, "html.parser")
		divsBody = bsoup.findAll("div", class_="subcategory-product-item__body")
		divsFooter = bsoup.findAll("div", class_="subcategory-product-item__footer")
		
		iCount = 0
		while iPage > 0 and len(divsBody) == len(divsFooter) and iCount < len(divsBody):
			divBody = divsBody[iCount]
			divFooter = divsFooter[iCount]
			
			dictProduct = {}
			
			dictProduct["img"] = divBody.find('div', {'class': 'wrap-img'})
			
			if dictProduct["img"]:
				dictProduct["img"] = dictProduct["img"].find("img")
				
				if dictProduct["img"].get("src"):
					dictProduct["img"] = dictProduct["img"].get("src")
				else:
					dictProduct["img"] = dictProduct["img"].get("data-src")
			
			div_product_info = divBody.find('div', {'class': 'product_name cms_item_panel subcategory-product-item__info'})
			dictProduct["link"] = div_product_info.find('a', {'class': 'link_gtm-js link_pageevents-js ddl_product_link'}).get("href")
			dictProduct["name"] = div_product_info.find('a', {'class': 'link_gtm-js link_pageevents-js ddl_product_link'}).text
			dictProduct["desc"] = div_product_info.find('p', {'class': 'short_description'}).text
			dictProduct["market"] = "Citilink";
			
			dictProduct["cost"] = divFooter.find('div', {'class': 'subcategory-product-item__price-container'}).find('span')
			
			if dictProduct["cost"]:
				dictProduct["cost"] = int(dictProduct["cost"].find('ins').text.replace(' ', '').replace(u'\\n', '').replace(u'руб.', ''))
				
			
				listProducts.append(dictProduct)
			else:
				iPage = -2
				break
			
			iCount += 1
			
		iPage += 1
		
		#if iPage >= 10:
			#break
			
	return listProducts
	
############################################################################
	
#парсер товаров для магазина Ulmart
def ParserUlmart(sLink):
	g = Grab()
	
	sPage = ""
	iPage = 1
	listProducts = []
	
	while 1:
		sCurrURL = sLink + "?pageNum=" + str(iPage)
		sPage = g.go(sCurrURL, reuse_cookies=1, cookiefile="cookies.txt", connect_timeout=1000, timeout=3000).body
		print(str(g.response.code) + " -- " + sCurrURL + "\n")
		if g.response.code != 200:
			break
			
		#f = open("_Ulmart" + ".html", 'w', encoding='utf-8')
		#f.write(g.response.body.decode("utf-8"))
		#f.close()
		
		bsoup = bs4.BeautifulSoup(sPage, "html.parser")
		divs = bsoup.findAll("div", class_="b-box__i")
		
		for div in divs:
			dictProduct = {}
			dictProduct["img"] = div.find('a', {'class': 'must_be_href double-hover js-gtm-product-click'}).find("img").get("src")
			dictProduct["link"] = "https://www.ulmart.ru" + div.find('div', {'class': 'b-product__title'}).find("a").get("href")
			dictProduct["name"] = div.find('div', {'class': 'b-product__title'}).find("a").text
			dictProduct["desc"] = div.find('div', {'class': 'b-product__descr'}).text
			dictProduct["cost"] = int(div.find('div', {'class': 'b-product__price'}).find('span').find('span').text.replace(' ', '').replace(u'\xa0', ''))
			dictProduct["market"] = "Ulmart";
			
			listProducts.append(dictProduct)
			
		iPage += 1
		
		listNavLinks = bsoup.findAll("a", class_="b-pagination__item b-pagination__item_edge")
		#print("len(listNavLinks) = " + str(len(listNavLinks)) + "|" + listNavLinks[len(listNavLinks) - 1].text.lower())
		
		if listNavLinks[len(listNavLinks) - 1].text.lower() != "вперед":
			break
		
		#if iPage >= 10:
			#break
			
	return listProducts