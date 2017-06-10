
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page, "lxml")
    return soupdata

def parse_site(data):
    for title in data.find_all('title'):
		return(title.text)
	for author in data.find_all('span', 'author'):
		return(author.text+ "\n")
   	for paragraph in data.find_all('p'):
   		return(paragraph.text)

#def parse_author(data):
#	for author in data.find_all('span', 'author'):
#		return(author.text+ "\n")
#
#def parse_paragraph(data):
#	for paragraph in data.find_all('p'):
#		return(paragraph.text)
#
#def parse_title(data):
#	for title in data.find_all('title'):
#		return(title.text)

























