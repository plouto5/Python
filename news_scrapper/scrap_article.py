import urllib
import urllib.request
from bs4 import BeautifulSoup

url_from_list = 'http://m.twins.mlb.com/news/article/231390532/twins-postponed-will-play-doubleheader-sunday/'

def make_soup(url):
	page = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(page, "lxml")
	return soupdata

soup = make_soup(url_from_list)

def scrape_site(soup):
	for title in soup.find_all('title'):
		print(title.text)
	for author in soup.find_all('span', 'author'):
		print(author.text+ "\n")
	for paragraph in soup.find_all('p'):
		print(paragraph.text)

scrape_site(soup)

