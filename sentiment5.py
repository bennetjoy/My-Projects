from nltk.tokenize import sent_tokenize
sentences = sent_tokenize('''I love this book! Though I hate the beginning. It would be great for you.''')   #spliting sentence
for s in sentences:
    print(s)
print(sentences)