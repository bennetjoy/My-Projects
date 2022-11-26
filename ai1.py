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
import client
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)
rate = engine.getProperty('rate')
engine.setProperty('rate',175
)

app_id = "6VYG33-H8U7RE68KY"

client = wolframalpha.Client(app_id)

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

    speak("I am Bella. An Artificial Intelligence created by the Information Technology Department. How may I help you")       

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
        print("Say that again please...")
        return "None"
        
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'who is ' in query or 'who is the Head of' in query or 'HRD' in query or 'HOD' in query or 'Head of' in query:
            speak('')
           
            if 'MBA' in query or 'Geo Baby' in query or 'jio baby' in query:
                speak('Doctor Geo Baby is the head of the MBA department')

            elif 'CSE' in query or 'CS' in query or 'computer science' in query or 'Amel Austine' in query:
                speak('mister Amel Austine is the head of the computer science department')

            elif 'triple E' in query or 'Electrical and Electronics'  in query or 'EEE' in query or 'B Aruna' in query:
                speak('Doctor B. Aruna is the head of the triple E department')
        
            elif 'ECE' in query or 'EC' in query or 'electronics and communication' in query or 'Smitha Cyriac' in query:
                speak('Missis Smitha Cyriac is the head of the electronics and communication department')

            elif  'information technology' in query or 'IT' in query or 'Anju Susan' in query:
                speak('missis Anju Susan George is the head of the information technology department')

            elif 'mech' in query or 'mechanical' in query or 'vinoj k' in query:
                speak('Mister Vinoj K is the head of the mechanical engineering department')

            elif 'civil' in query or 'CE' in query or 'shine george' in query:
                speak('Missis Shine George is the head of the civil engineering department')

            elif 'science and humanities' in query or 's and h' in query or 'Ann Neetha Sabu' in query:
                speak('Missis Ann Neetha Sabu is the head of the S and H department')
                

        elif 'your name' in query or 'who are you' in query:
            speak('I am BELLA. An Artificial intelligence created by the Information Technology Department of Vishwa Jyoti College of Engineering and Technology. ')

        elif 'direct me to' in query or 'where is' in query or 'where can i find' in query or 'way to' in query or 'navigate' in query:
            speak('sure')

            if 'vice principal' in query:
                speak('The vice principles office is located in the second floor of , B block. Room number B 2 2 0')

            elif 'principal' in query:
                speak('The principles office is located on the second floor of B block, Room number B 2 0 2')

            elif 'library' in query:
                speak('You can enter the Library through the main entrance of the B block')

            elif 'staff room' in query or 'Department room' in query:
                
                if 'IT' in query or 'Information technology' in query:
                    speak('The staff room of the Information technology department is located on the first floor of A block, Room number A 1 0 2')
                    
        elif 'vice principal' in query or 'somy' in query:
            speak('Mr. somy p mathew is the vice principal of this college')

        elif 'principal' in query or 'Joseph Kunj paul c' in query:
            speak('doctor joseph kunjupaul c is the principal of this college')

        elif 'bye' in query or 'see ya' in query or 'see you' in query:

            if hour>=19 and hour<=0:
                speak('Good Night')
            else:
                speak('Good bye')

        elif 'NBA accreditation' in query or 'NBA' in query or 'accreditation' in query or 'accredited' in query:
                speak('vishva jyothi college of engineering and technology has its all b tech, and management cource, acreditted by the national board of acreditation, or n b a')

        elif 'about college' in query or 'about vishva jyoti' in query or 'about v j c e t' in query:
                speak('vishva jyothi college of engineering and technology, V J C E T is yet another hallmark of the commitment, and experience of the catholic dioces of kothamangalam in the field of education. Established in the year 2001, as a self financing engineering college affiliated to mahatma gandhi university and later in 2015, affiliated to a p j abdul kalam technological university, had grown manifolds and has earned reputation as a trend setter in engineering and management education. The college is situated in a sprawling campus of 26 acres, nested among lush greenery over a hillock on the side of state highway number 8.')

        elif 'how do you do' in query:
            speak('How do you do')

        elif 'what\s up' in query or 'how are you' in query or 'whatsapp' in query:
            stMsgs = ['just doing my things', 'i am fine', 'i am great', 'i am full of energy']
            speak(random.choice(stMsgs))

        elif 'Bennet' in query or 'bennett' in query:
            speak('Bennet Joy is my creater')

        elif 'vision' in query:
            speak('MOULDING ENGINEERS par EXCELLENC WITH INTEGRITY, FAIRNESS, AND HUMAN VALUES')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H hours and %M minutes")
            speak(f"the time is {strTime}")

        elif 'question' in query: #on trial #wolframalpha
            res = client.query(query)
            results = next(res.results).text
            speak('wolfram alpha says')
            speak(results)

        elif 'when is' in query or 'what is' in query or 'which is' in query or 'tell me about' in query or 'speak on' in query or 'speak about' in query:
            speak('lets see...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'explain' in query or 'briefly describe' in query:
            speak('ok')
            result = wikipedia.summary(query,sentences=6)
            speak(result)

        elif 'bella' in query or 'hi' in query or 'hello' in query or 'hey' in query:
            stMsgs = ['Hi', 'Hello', 'Whats up']
            speak(random.choice(stMsgs))

        elif 'who created you' in query or 'whose your maker' in query or 'who is your creater' in query:
            speak('bennet joy from information technology department created me')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'thank you' in query:
            speak('you are welcome')

        elif 'love you' in query:
            speak('love you too')


        elif 'play music' in query:
            speak('playing music')
            music="d:\\songs\\song01.mp3"
            os.startfile(music)

        elif 'open code' in query or 'chord' in query:
            speak('you are not authorised to make any changes or to view the code')
        
        elif 'f***' in query:
            speak('You are not allowed to use unparliamentary words inside the campus')

        elif 'shutdown' in query or 'power off' in query or 'Turn off' in query:
            speak('You have to use your authorisation code to do that.')

            if '2001' in query:
                speak('command accepted')
                speak('System Shutting Down')
                sys.exit()

        elif 'what can you do' in query:
            speak('I am a trial version. But still you can say, navigate me to the principles office, what is an internal combustion engine, or any such commands. ')

        elif 'joke' in query:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')