import urllib.request
from bs4 import BeautifulSoup


def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page, "lxml")
    return soupdata

def parse_site(data,mail):

	
	for title in data.find_all('title'):
		mail.write(title.text)
	for author in data.find_all('span', 'author'):
		mail.write(author.text+'\n\n')
	for paragraph in data.find_all('p'):
		mail.write(paragraph.text)
			

