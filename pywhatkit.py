import pywhatkit

fln = input("Enter file name:")

file = open('fln','r')

str = file.read()

pywhatkit.text_to_handwriting(str,"pytexthand.png",[10,10,10])