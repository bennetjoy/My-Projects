import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser 
import os
import smtplib
import pyaudio
import random
import sys
import wolframalpha
import subprocess
import re
from gtts import gTTS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)
rate = engine.getProperty('rate')
engine.setProperty('rate',180)

def speak(audio):
    print('John: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')
    
    speak("I am John, Your personal artificial intelligence")
     
greetMe()

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()
        
        if 'change your name' in query:
		    username = myCommand()
            if "bennett" in username:

                try:
			    speak("please verify your password")
			    password = myCommand()

			    if "bellagio 2001" in password:
			        speak("verified. Welcome Bennet Joy")
		 
          
