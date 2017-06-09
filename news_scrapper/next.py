import urllib
import urllib.request
from bs4 import BeautifulSoup
import datetime
from datetime import date, timedelta

today = datetime.date.today()
yesterday = datetime.date.today() - timedelta(1)

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page, "xml")
    return soupdata

soup = make_soup('http://mlb.mlb.com/partnerxml/gen/news/rss/min.xml')

articles = []
obj_list = []

for item in soup.findAll('item'):
    for t in item.findAll(['title', 'link', 'mlb:display-date']):
        articles.append(str(t.text))

i = 0
var_list = []
while i<len(articles):
    var_list.append(articles[i:i+3])
    i+=3
for date in var_list:
    date[2] = datetime.datetime.strptime(date[2][:-4], '%m/%d/%Y %I:%M ')

class reporter:

    def __init__(self,title,link,disdate):
        self.title = title
        self.link = link
        self.date = disdate
        
for x in var_list:
	obj = reporter( x[0], x[1], x[2])
	obj_list.append(obj)

	
yester_day = datetime.datetime.strptime(yesterday, '%m/%d/%Y %I:%M ')
final_articles = []
print(type(yesterday))
print(type(yester_day))

#for i in obj_list:
#	if i.date >= yester_day:
#		final_articles.append(i.link)
		
#print(final_articles)





















