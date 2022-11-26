import pandas as pd

fh = pd.read_csv(r"C:\\Users\\Bennet Joy\\OneDrive\\Documents\\book1.csv")
df = pd.DataFrame(fh,columns=['words'])
print(df)


import re

def depure_data(data):
    
    #Removing URLs with a regular expression
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    data = url_pattern.sub(r'', data)

    # Remove Emails
    data = re.sub('\S*@\S*\s?', '', data)

    # Remove new line characters
    data = re.sub('\s+', ' ', data)

    # Remove distracting single quotes
    data = re.sub("\'", "", data)
        
    return data

data = input("enter your data: ")

x = depure_data(data)
print(x)