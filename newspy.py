import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=3a89dcb6253f4fd999c188e3ed4e7138')
response = requests.get(url)
print response.json()