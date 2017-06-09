
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page, "lxml")
    return soupdata

def parse_site(data):
    for title in data.find_all('title'):
        print(title.text)
    for author in data.find_all('span', 'author'):
        print(author.text+ "\n")
    for paragraph in data.find_all('p'):
        print(paragraph.text)



























