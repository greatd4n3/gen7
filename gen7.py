import scrapy 

class quotescraper(scrapy.Spider):
	name = 'gen5'
	start_urls = ['https://www.ebay.com/sch/areatrend/m.html?_nkw&_armrs=1&_ipg&_from&LH_BIN=1&rt=nc&_udlo&_udhi&LH_PrefLoc=98&LH_Sold=1&LH_Complete=1']
	CONCURRENT_ITEMS = 4
	CONCURRENT_REQUESTS = 4
# above url can be changed to ebay page you want to use. Should work on any sellers page with the options 'buy it now + sold' selected.
# concurrent items/requests was set in an attempt to simplify the output. this has not worked as intended. 

	def parse(self,response):
		for title in response.xpath('//div[@id="ResultSetItems"]'):
			link = {
			'link':title.xpath('//h3/a[@class="vip"]/@href').extract_first(), 
			#'title':title.xpath('//a[@class="vip"]//text('')').extract(),
			#'price':title.xpath('normalize-space(//span[@class="bold bidsold"]//text())').extract(), 
			#'listprice':title.xpath('//span[@class="stk-thr"]//text()').extract(),
			}

#yield title
		for i in response.xpath('//div[@id="ResultSetItems"]'):
			title = {
			'title':i.xpath('//a[@class="vip"]//text('')').extract_first(),
			}
#yield price 
		for i in response.xpath('//div[@id="ResultSetItems"]'):
			price = {
			'price':i.xpath('normalize-space(//span[@class="bold bidsold"]//text())').extract_first(),
			}

		yield link
		yield title
		yield price

# trying to clean the output for multiple items. 
# attempted to create individual for loops and yield individual output
# Not working well. 
