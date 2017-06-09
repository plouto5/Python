import urllib
import urllib.request
from bs4 import BeautifulSoup
import datetime
from datetime import date, timedelta

#################### Load XML ##########################
def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page, "xml")
    return soupdata

soup = make_soup('http://mlb.mlb.com/partnerxml/gen/news/rss/min.xml')
########################################################

#################### Link Scrub ########################
final_articles = []
articles = []
obj_list = []

today = datetime.datetime.today()
yesterday = datetime.datetime.today() - timedelta(days=1,)#hours=12


class reporter:

    def __init__(self,title,link,disdate):
        self.title = title
        self.link = link
        self.date = disdate
 
 
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
        
for x in var_list:
	obj = reporter( x[0], x[1], x[2])
	obj_list.append(obj)

for i in obj_list:
	if i.date >= yesterday:
		final_articles.append(i.link)
#########################################################





















