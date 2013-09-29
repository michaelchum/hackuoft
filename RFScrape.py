__author__ = 'ivanfer'

# all imports are missing everywhere

def HARD_URL(args):
    pass


class RFScrape:
    """# this class will contain the controller to scrapy
    # and maintain all of the Posts in a datastructure.
    # returns the result of scraping to RFAlert.
    """
    HARD_URL = "forums.redflagdeals.com/hot-deals-f9"

    def __init__(self):
        self.scraper = Scraper(RFScrape.HARD_URL)
        pass
