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

for i in soup.findAll('item'):
	for t in i.findAll(['title', 'link', 'mlb:display-date']):
		print(str(t.text)[0])
