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


for item in soup.findAll('item'):
	for t in item.findAll(['title', 'link', 'mlb:display-date']):
		articles.append(str(t.text))



# Take list into nested lists


i = 0
var_list = []
while i<len(articles):
	var_list.append(articles[i:i+3])
	i+=3

good_article = []
current_day = today.strftime('%m/%d/%Y')
yester_day = yesterday.strftime('%m/%d/%Y')

for datetime in var_list:
	print(datetime[2])


