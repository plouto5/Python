import urllib
import urllib.request
from bs4 import BeautifulSoup
import datetime
from datetime import date, timedelta

today = datetime.date.today()
yesterday = date.today() - timedelta(1)

def make_soup(url):
	page = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(page, "xml")
	return soupdata

soup = make_soup('http://mlb.mlb.com/partnerxml/gen/news/rss/min.xml')

articles = []
good_articles = []

class reporter:
	
	def __init__(self,title,link,disdate):	
		self.title = title
		self.link = link
		self.date = disdate
		self.data = data


for t in soup.findAll(['title', 'link', 'mlb:display-date']):
	obj = reporter(str(t.text)[0],str(t.text)[1],datetime.datetime.strptime(str(t.text)[2], '%m/%d/%Y'))
#	obj.title = t[0]
#	obj.link = t[1]
#	obj.displayDate = date(t[2], '%M/%d/%Y')
	articles.append(obj)

print(articles)




