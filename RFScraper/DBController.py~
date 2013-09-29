import sqlite3
from RFScraper import *
import os
import sqlite3

class DBController:
    """
    interface between RFAlert and database
    """

    insert_temp = 'INSERT INTO RFPost VALUES (? , ? , ?)'

    def __init__(self):
        self.conn = sqlite3.connect('miuDB.db')
        self.c = conn.cursor()
        # create tables here???
        self.c.execute("""CREATE TABLE IF NOT EXISTS Users (email varchar(30) primary key, words varchar(30) )""")
		self.c.execute("""CREATE TABLE IF NOT EXISTS Keywords (words varchar(30) primary key )""")
		self.c.execute("""CREATE TABLE IF NOT EXISTS RFPosts ( id INTEGER PRIMARY KEY AUTOINCREMENT, title varchar(30), url varchar(30) UNIQUE) """)	
		self.c.execute("""CREATE TABLE IF NOT EXISTS RFUsers (email varchar(30) , words varchar(30), primary key(email, words), FOREIGN KEY(email) REFERENCES Users(email), FOREIGN KEY(words) REFERENCES RFPosts(title)) """)
		self.conn.commit()
		self.c.close()

        #pass
        #initialize cursors here. Makes sure there's only one controller interacting with database

    def getkeywords(self): #TODO
        """
        fetches DB for keywords and corresponding emails.

        SELECT keyword, email FROM email
        ORDER BY keyword

        IMPLEMENTED BY USMAN
        """
        c1 = self.conn.cursor()
		result1 = c1.execute('SELECT * FROM Users')	
		dict_words = {}
		for r in result1.fetchall():
			c2 = self.conn.cursor()
			result2 = c2.execute('SELECT * FROM Keywords')	
			for k in result2.fetchall():
				if k[0] == r[1]:
					m = k[0]
					if not (m in dict_words.keys()):
						dict_words[m] = []
					dict_words[m].append(r[0])
		self.conn.commit()
		return dict_words;

        

    def insert_rfpost(self, hash_id, title, url ):
		self.c.execute("INSERT INTO RFPosts VALUES (? , ? , ?)", (hash_id, title, url))
		self.conn.commit()

    def addrelation(self, user, post):
        """returns whether tuple already existed in DB
        @return:

        """
        try:
            self.cur.execute(DBController.insert_temp, (user.key(), post.title()))
        except sqlite3.IntegrityError:
            pass

    
