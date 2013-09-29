__author__ = 'ivanfer'


'''class Scraper(object):
    """
        all scrapy done in here. dont know what those objects look like so i haven't instantiated them.
    """
    home_url = ''

    def __init__(self, url):
        self.home_url = url

    def scrape(self, scraped_title,scraped_url):
        #myPost = Post(scraped_title, scraped_url)
	crawler = URLSpider(BaseSpider)'''

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field
from scrapy.cmdline import execute

class URLSpider(BaseSpider):
	name = 'URLparse'
	start_urls = ['http://forums.redflagdeals.com/hot-deals-f9/' ]
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//ul/li')
		items = []
		for site in sites:
			#item1 = URLItem()
			item1 = site.select('a/text()').extract()
			print item1
           	item2 = site.select('a/@href').extract()
		self.Post(item1, item2)
           	print item2
           	#items.append(item)

if __name__ == "__main__":
	execute(['scrapy', 'crawl', 'URLparse'])

	


