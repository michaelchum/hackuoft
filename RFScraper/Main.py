__author__ = 'ivanfer'

from RFScrape import scrapeRFD
from MailAlert import mailAll

def main():
	#dbc = DBController()
	adbc = "jhfjsd"
	users = scrapeRFD(adbc)
	mailAll(users)

if __name__ == "__main__":
    main()
