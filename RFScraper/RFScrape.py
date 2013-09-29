

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
            #assert isinstance(p.title().split, dict)
            split = p.title().split()
            for s in split:
                if s in keywords.keys():
                    for u in keywords[s]:
                        user = User.init(u)
                        if not dbc.addrelation(user, p):
                            if not users.contains(user):
                                user.addPost(p)
                                users.append(user)

        return users
        #all new posts in db associated to an email






