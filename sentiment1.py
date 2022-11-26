from textblob import TextBlob

text = input("Enter the text to analyse:")
analysis = TextBlob(text)
if analysis.sentiment.polarity > 0:
    x = "positive"
elif analysis.sentiment.polarity < 0:
    x = "negative"
else:
    x = "neutral"

print("The text is",x)