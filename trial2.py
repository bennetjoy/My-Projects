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
import warnings
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)
rate = engine.getProperty('rate')
engine.setProperty('rate',176)

warnings.filterwarnings('ignore')

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()
soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")

def speak(audio):
    print('Bella: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good evening!")  

    speak("I am Bella. How may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'your name' in query:
            speak('hi , i am bella.')

        elif 'news' in query or 'update me' in query:
            for news in news_list:
                #print(news.link.text)     #weblink of news
                print("-"*85)
                speak(news.title.text)
                print(news.pubDate.text)
       