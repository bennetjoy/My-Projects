#lemmatize

from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer

stokens = ['#hello','i','am','bennet','joy','and','ran','a','lot','today','running']
def lemmatize_sentence(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
    return lemmatized_sentence

print(lemmatize_sentence(stokens))
