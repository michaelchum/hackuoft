__author__ = 'michaelchum'

from bs4 import BeautifulSoup
import urllib2
import re
import unicodedata
from Post import Post
from PostList import PostList
 
def scrape():
	urlList=[]
	urlList.append("http://forums.redflagdeals.com/hot-deals-f9/")

	#for x in range(9):
		#urlList.append("http://forums.redflagdeals.com/hot-deals-f9/%d/" % (x+2))

	postList = PostList()

	for x in range(len(urlList)):
		content = urllib2.urlopen(urlList[x]).read()
		soup = BeautifulSoup(content)

		for link in soup.findAll(True, {'class': re.compile(r'\btitle\b')}):
		    url = "http://forums.redflagdeals.com" + link.get('href')
		    title = link.get_text()
		    title = title.replace(u'\xae', u' ')
		    title = title.replace(u'\xa2', u' ')
		    title = title.encode('ascii', 'ignore')
		    post = Post(title, url)
		    postList.addPost(post)
	return postList
