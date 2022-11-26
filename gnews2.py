from GoogleNews import GoogleNews


"""googlenews = GoogleNews()
googlenews = GoogleNews(lang='en')
googlenews = GoogleNews(period='7d')
googlenews = GoogleNews(start='02/01/2020',end='02/28/2020')
googlenews = GoogleNews(encode='utf-8')"""

#or

googlenews.set_lang('en')
googlenews.set_period('7d')
googlenews.set_time_range('02/01/2020','02/28/2020')
googlenews.set_encode('utf-8')

googlenews.get_news('APPLE')
googlenews.search('APPLE')

googlenews.get_page(2)
result = googlenews.page_at(2)

googlenews.total_count()

googlenews.results()
googlenews.get_texts()

