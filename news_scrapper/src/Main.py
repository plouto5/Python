import soup
import parse


url_list = 'http://mlb.mlb.com/news/article/min/twins-top-orioles-with-ervin-santanas-shutout?ymd=20170523&content_id=231986710&vkey=news_min'

data = soup.make_soup(url_list)

parse.parse_site(data)

''' add functions and classes to find the articles
	to populate the url_list. Then out put to file
	or email to recipient.
'''









