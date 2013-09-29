from bs4 import BeautifulSoup
import urllib2
import re
import unicodedata
 
urlList=[]
urlList.append("http://forums.redflagdeals.com/hot-deals-f9/")

for x in range(9):
	urlList.append("http://forums.redflagdeals.com/hot-deals-f9/%d/" % (x+2))

for x in range(len(urlList)):
	content = urllib2.urlopen(urlList[x]).read()
	soup = BeautifulSoup(content)

	for link in soup.findAll(True, {'class': re.compile(r'\btitle\b')}):
	    url = "http://forums.redflagdeals.com" + link.get('href')
	    title = link.get_text()
	    title = title.replace(u'\xae', u' ')
	    print url
	    print title


