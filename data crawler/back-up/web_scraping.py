from bs4 import BeautifulSoup
import urllib.request

url =  'https://vnexpress.net'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

new_feeds = soup.find(
	'section', class_='section section_stream_home section_container').find_all('a')

for feed in new_feeds:
    title = feed.get('title')
    link = feed.get('href')
    content = feed.contents[0]
    print('Title: {} - content: {} -Link: {}'.format(title, content, link))
