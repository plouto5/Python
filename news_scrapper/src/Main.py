import soup
import parse



def scrape_article(url):
	data = soup.make_soup(url)
	x = parse.parse_site(data)
	return(x)	
''' add functions and classes to find the articles
	to populate the url_list. Then out put to file
	or email to recipient.
'''









