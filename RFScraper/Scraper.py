
from RFScraper import *

class Scraper(object):
    """
        all scrapy done in here. dont know what those objects look like so i haven't instantiated them.
    """

    def __init__(self, url):
        self.home_url = url

    @staticmethod
    def scrape():
        return PostList()
