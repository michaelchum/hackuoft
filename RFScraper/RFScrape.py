

# all imports are missing everywhere

from PostList import *
from Post import Post
from Scraper import scrape
from User import User


"""# this class will contain the controller to scrapy
# and maintain all of the Posts in a datastructure.
# returns the result of scraping to RFAlert.
"""

def scrapeRFD(dbc):

    newposts = scrape()
    keywords = dbc.getkeywords() #assuming a string:[string] dictionary
    #keywords = {"Samsung":["usman.ehtesham@mail.mcgill.ca","sanchezivanf@gmail.com","michael.ho@mail.mcgill.ca"]}
    users = []

    for p in newposts:
        #assert isinstance(p.title().split, dict)
        split = p.title
        split = split.split()
        for s in split:
            if s in keywords.keys():
                for u in keywords[s]:
                    user = User(u)
                    if not dbc.addrelation(user, p):
                        if not user in users:
                            user.addPost(p)
                            users.append(user)

    return users
    #all new posts in db associated to an email






