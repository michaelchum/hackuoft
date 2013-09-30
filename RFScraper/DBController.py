import sqlite3
import os
from Scraper import scrape


class DBController:

    insert_temp = 'INSERT INTO RFPost VALUES (? , ?)'

    def __init__(self):
        self.conn = sqlite3.connect('miuDB.db')
        self.c = self.conn.cursor()
        # create tables here???
        
        self.c.execute("""CREATE TABLE IF NOT EXISTS Users (email varchar(30), words varchar(30), primary key (email,words) )""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS Keywords (words varchar(30) primary key )""")
    	self.c.execute("""CREATE TABLE IF NOT EXISTS RFPosts ( title varchar(30) primary key, url varchar(30) UNIQUE) """)
    	self.c.execute("""CREATE TABLE IF NOT EXISTS RFUsers (email varchar(30) , title varchar(30), primary key(email, title), FOREIGN KEY(email) REFERENCES Users(email), FOREIGN KEY(title) REFERENCES RFPosts(title)) """)
    	self.conn.commit()
        
        self.c.close()

        #pass
        #initialize cursors here. Makes sure there's only one controller interacting with database

    def getkeywords(self):
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
            self.c.execute(DBController.insert_temp, (user.key(), post.title()))
        except sqlite3.IntegrityError:
            pass

    
