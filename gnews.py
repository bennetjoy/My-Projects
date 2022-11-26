import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
news_url="https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US"   # till rss will give global headlines
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()
soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
for news in news_list:
    print("-"*85)
    print(news.title.text)
    print(news.pubDate.text)
    #print(news.link.text)
