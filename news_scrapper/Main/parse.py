

def parse_site(data):
	for title in data.find_all('title'):
		print(title.text)
	for author in data.find_all('span', 'author'):
		print(author.text+ "\n")
	for paragraph in data.find_all('p'):
		print(paragraph.text)


