__author__ = 'ivanfer'

from RFScraper import *
from Notifier import *

def main():
        """
        The big cheese.
        1. make sure all users are accounted for (eg import from DB)
        2.

        """
        dbc = DBController()
        users = RFScrape.scrapeRFD(dbc)
        Notifier.notify(users)

if __name__ == "__main__":
    main()
