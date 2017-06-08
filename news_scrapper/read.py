import urllib
import urllib.request
from bs4 import BeautifulSoup



def make_soup(url):
	page = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(page, "xml")
	return soupdata

soup = make_soup('http://mlb.mlb.com/partnerxml/gen/news/rss/min.xml')



title = []
url = ""
pubDate = ""




for item in soup.findAll('item'):
	for t in item.findAll(['title', 'link', 'pubDate']):
		title.append(str(t.text))

# Take list into nested lists

i = 0
var_list = []
while i<len(title):
	var_list.append(title[i:i+3])
	i+=3

print(var_list[0])
#print(title[0])

if 'Apr' in var_list[2]:
	print('True')



