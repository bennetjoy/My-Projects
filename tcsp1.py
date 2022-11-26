pos = ['good','happy','best','laugh','loved','love','beautiful','thanks','enhance','plus','thank you','thankyou','nice','entertaining','excellent','awesome','satisfied','very','superb','super','much','verymuch', 'enjoyed','laughed','liked']
neg = ['sad','but','bad','crying','worst','hate','hated','unhealthy','disappoinment','disappoint','disappointed','cheat','cheating','fraud','nasty','please','tolerate','unhappy','minus','not','unsatisfied','tolerate','patience','waste','cheap']

negcount = 0
poscount = 0

w = str(input("Please provide your feedback:"))
w = w.lower()
wl = list(w.split(" "))

for i in wl:
    for j in pos:
        if i==j:
            poscount = poscount+1
    for k in neg:
        if i==k:
            negcount = negcount+1

tf = negcount + poscount
np = (negcount/tf)*100
pp = (poscount/tf)*100

if(poscount > negcount):
    fedbk = "Good"
    rate = pp
elif(poscount<negcount):
    fedbk = "Bad"
    rate = np
else:
    fedbk = "Neutral"
    rate = 0.0

print("The over all feed back is",fedbk)
print(rate,"%")