__author__ = 'ivanfer'

from RFScrape import scrapeRFD
from MailAlert import mailAll
from DBController import DBController

def main():
	dbc = DBController()
	#adbc = "jhfjsd"
	users = scrapeRFD(dbc)
	mailAll(users)

if __name__ == "__main__":
    main()
