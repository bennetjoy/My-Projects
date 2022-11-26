from textblob import TextBlob
import nltk
from newspaper import Article

#Get the article
url = 'https://everythingcomputerscience.com/'
article = Article(url)

# Do some NLP
article.download() #Downloads the link’s HTML content
article.parse() #Parse the article
nltk.download('punkt')#1 time download of the sentence tokenizer
article.nlp()#  Keyword extraction wrapper

text = article.summary
#print text
print(text)