import scrape_articles




def scrape(url):
	data = scrape_articles.make_soup(url)
	x = scrape_articles.parse_site(data)
	return(x)	




''' add functions and classes to find the articles
	to populate the url_list. Then out put to file
	or email to recipient.
'''









