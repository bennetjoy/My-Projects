import pyttsx3
import datetime
import wikipedia
import pyaudio

engine = pyttsx3.init()
volume = engine.getproperty('volume')
engine.setproperty('volume', volume-0.25)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()