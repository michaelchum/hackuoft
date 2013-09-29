

# all imports are missing everywhere

from RFScraper import *

class RFScrape:
    """# this class will contain the controller to scrapy
    # and maintain all of the Posts in a datastructure.
    # returns the result of scraping to RFAlert.
    """
    hard_url = "forums.redflagdeals.com/hot-deals-f9/"

    def scrapeRFD(dbc):

        scraper = Scraper(RFScrape.hard_url)
        newposts = scraper.scrape()
        keywords = dbc.getkeywords() #assuming a string:[string] dictionary
        users = []

        for p in newposts:
            assert isinstance(p.title().split, dict)
            split = p.title().split()
            for s in split:
                if s in keywords.keys():
                    for u in keywords[s]:
                        assert isinstance(u,Post)
                        if not dbc.addrelation(u, p):
                            if not users.contains(u):
                                u.addPost(p)
                                users.append(u)

        return users
        #all new posts in db associated to an email






