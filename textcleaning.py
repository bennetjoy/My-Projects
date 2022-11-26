
text2 = input("Enter your text here: ")

#cleantext
import cleantext 
from nltk import text

k = cleantext.clean_words(text2,
all= False, # Execute all cleaning operations
extra_spaces=True ,  # Remove extra white space 
stemming=True , # Stem the words
stopwords=True ,# Remove stop words
lowercase=True ,# Convert to lowercase
numbers=True ,# Remove all digits 
punct=True ,# Remove all punctuations
stp_lang='english'  # Language for stop words
)
#l = cleantext.clean(text, all= True) 
print(k)

#clean-text

"""from cleantext import clean

k = clean(text,lower=True,no_urls=True,replace_with_digit=" ").split(" ")
print(k)"""

