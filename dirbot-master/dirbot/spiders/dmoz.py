from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from Post import Post
from PostList import PostList

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://forums.redflagdeals.com/hot-deals-f9/",
        "http://forums.redflagdeals.com/hot-deals-f9/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        hxs = HtmlXPathSelector(response)
        #sites = hxs.select('//ul[@class="directory-url"]/li') 
        sites = hxs.select('//ul[@class="threads_list"]/li')
        #sites2 = hxs.select('//a[@class="title threadtitle_unread"]/li') 

        postList = PostList()

        for site in sites:
            post = Post(site.select('a[@class="thread_title"]/text()').extract(), 
                site.select('a/@href').extract())
            #postList.addPost(post)
            print post.title
            print post.url

        #RFScraper(postList)
