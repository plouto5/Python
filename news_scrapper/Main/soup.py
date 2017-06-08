import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
	page = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(page, "lxml")
	return soupdata
