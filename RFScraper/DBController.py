import sqlite3
from RFScraper import *


class DBController:
    """
    interface between RFAlert and database
    """

    insert_temp = 'INSERT INTO RFPost VALUES (? , ? , ?)'

    def __init__(self):
        pass
        #initialize cursors here. Makes sure there's only one controller interacting with database

    def getkeywords(self): #TODO
        """
        fetches DB for keywords and corresponding emails.

        SELECT keyword, email FROM email
        ORDER BY keyword

        IMPLEMENTED BY USMAN
        """
        return {} #TODO

    def addrelation(self, user, post):
        """returns whether tuple already existed in DB
        @return:

        """
        try:
            self.c.execute(DBController.insert_temp, (user.key(), post.title()))
        except sqlite3.IntegrityError:
            pass
