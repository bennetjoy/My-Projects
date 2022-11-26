st = "hello my name is bennet joy"
b = []
k = st.replace(" ","")
for i in k:
    b.append(i)
a=b.count('a')
e=b.count('e')
i=b.count('i')
o=b.count('o')
u=b.count('u')
v=a+e+i+o+u
c=len(b)-v
w=len(st.split())
qn=b.count("?")
print("Vowels:",v)
print("Consonants:",c)
print("Words:",w)
print("Question marks:",qn)