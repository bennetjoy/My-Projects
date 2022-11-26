import cleantext 

from nltk import text

from nltk.tag import pos_tag

import pandas as pd

from datetime import datetime



start_time = datetime.now()

file = pd.read_csv("C:\\users\\bennet joy\\onedrive\\documents\\pypgm\\posneg.csv")

text1 = input("Enter your text: ")

print("This may take a few minutes as there is a lot of train data. Please be Patient! ")


#cleantext

def clean(t):
	ct = cleantext.clean_words(t,
	all= False,
	extra_spaces=True , 
	stemming=True , 
	stopwords=True ,
	lowercase=True ,
	numbers=True , 
	punct=True ,
	stp_lang='english'  
	)

	return ct


text2 = clean(text1)

#text3 = pos_tag(text2)


h = file.head(4783)

poscount = negcount = pos = neg = pc = nc = 0


for i in h.posword:
    for j in h.negword:
        for k in text2:
            if k==i:
                poscount = poscount+1
                pc = poscount/4783
            if k==j:
                negcount = negcount+1
                nc = negcount/4783

#print(pc,nc)
#print(text2)

# naive bayes: P(A/B)=(P(B/A)*P(A))/P(B)

pt = pc+nc  

# from basic idea 

if pt == 0:
	print("The Text is Neutral")

elif pc!=0 and nc==0:
	print("The Text is Positive")

elif pc==0 and nc!=0:
	print("The Text is Negative")

#applying naive bayes theorem

else:

	Pa = pc/pt

	Pb = nc/pt

	Pba = Pa/Pb

	Pab = (Pba*Pa)/Pb

	print(Pab)

	if Pab>1:
		print("The Text is Positive")

	elif Pab<1:
		print("The Text is Negative")

	else:
		print("The Text is Neutral")

end_time = datetime.now()

print('Execution time: {}'.format(end_time - start_time))
