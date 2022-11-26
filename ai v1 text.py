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

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)
rate = engine.getProperty('rate')
engine.setProperty('rate',176)

warnings.filterwarnings('ignore')

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

    speak("I am Bella. An artificial intelligence created by the Information Technology department. How may i help you")       

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
        print(e)    
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

def appointment():
    yn = input("Enter your name:")
    regno = input("Enter Reg No.")
    name = input("Enter recepient name:")
    tim = input("Enter time slot: FN/AN")
    sub = input("Enter subject:")
    lst1 = ['juliet@vjcet.org','anitta@vjcet.org']
    eid = "juliet@vjcet.org"
    if name == "juliet":
        eid = lst1[0]
    elif name == "anitta":
        eid = lst1[1]

    textdata = yn +"(" +regno + ")" + "has requested for an appointment at "+ tim + " session. Request has been sent to "+ eid + "." 
    print(textdata)
    speak("Email has been sent successfully")

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'your name' in query:
            speak('hi , i am bella.')

        elif 'direct me to' in query or 'where is' in query or 'where can i find' in query or 'way to' in query:
            

            if 'vice principal' in query:
                speak('The vice principles office is located in the third floor of , B block. Room number B 2 0 3')

            elif 'principal' in query:
                speak('The principles room is located on the third floor of B block, Room number B 2 0 4')


        elif 'vice principal' in query or 'somy' in query:
            speak('Mr. Somy P Mathew is the vice principal of this college')

        elif 'principal' in query:
            speak('Professor K K Rajan is the principal of this college')

        elif 'former principal' in query or 'Joseph Kunj paul c' in query:
            speak('doctor joseph kunjupaul c is the former principal of this college till 2020')

        elif 'bye' in query or 'see ya' in query or 'see you' in query:
            speak('Good bye')

        elif 'HOD of MBA' in query or 'head of the MBA' in query or 'HOD of the MBA' in query or 'Geo Baby' in query or 'jio baby' in query:
            speak('Doctor Geo Baby is the head of the MBA department')
 
        elif 'NBA accreditation' in query or 'NBA' in query or 'accreditation' in query or 'accredited' in query:
            speak('vishva jyothi college of engineering and technology has its all b tech, and management cource, acreditted by the national board of acreditation, or n b a')

        elif 'about college' in query or 'about vishva jyoti' in query or 'about v j c e t' in query:
            speak('vishva jyothi college of engineering and technology, V J C E T is yet another hallmark of the commitment, and experience of the catholic dioces of kothamangalam in the field of education. Established in the year 2001, as a self financing engineering college affiliated to mahatma gandhi university and later in 2015, affiliated to a p j abdul kalam technological university, had grown manifolds and has earned reputation as a trend setter in engineering and management education. The college is situated in a sprawling campus of 26 acres, nested among lush greenery over a hillock on the side of state highway number 8.')

        elif 'HOD of CSE' in query or 'HOD of CS' in query or 'head of CSE' in query or 'HOD of computer science' in query or ' head of computer science' in query or 'head of CS' in query or 'Amel Austine' in query:
            speak('mister Amel Austine is the HOD of the computer science department')

        elif 'HOD of triple E' in query or 'HOD of Electrical and Electronics'  in query or 'h o d of triple E' in query or 'head of triple E'  in query or 'head of electrical and electronics' in query or 'B Aruna' in query:
            speak('Doctor B. Aruna is the HOD of the triple E department')
        
        elif 'HOD of ECE' in query or 'HOD of EC' in query or 'head of ECE'  in query or 'head of EC' in query or 'head of electronics and communication' in query or 'HOD of electronics and communication' in query or 'H O D of electronics and communication' in query or 'Smitha Cyriac' in query:
            speak('Miss Smitha Cyriac is the HOD of the electronics and communication department')

        elif  'head of information technology' in query or 'head of the information technology' in query or 'HOD of IT' in query or 'head of IT' in query or 'head of Information Technology' in query or 'Anju Susan' in query:
                speak('Miss Anju Susan George is the HOD of the information technology department')

        elif 'HOD of mech' in query or 'HOD of mechanical' in query or 'head of mech' in query or 'head of mechanical' in query or 'vinoj k' in query:
            speak('Mister Vinoj K is the HOD of the mechanical engineering department')

        elif 'HOD of civil' in query or 'head of civil' in query or 'shine george' in query:
            speak('Missis Shine George is the head of the civil engineering department')

        elif 'HOD of science and humanities' in query or 'head of science and humanities' in query or 'Ann Neetha Sabu' in query:
            speak('Missis Ann Neetha Sabu is the head of the S and H department')

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
            
        elif 'when is' in query or 'who is' in query or 'which is' in query or 'tell me about' in query or 'speak on' in query or 'speak about' in query:
            speak('lets see...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)

        elif 'who created you' in query or 'who is your maker' in query or 'who is your creater' in query:
            speak('bennet joy from information technology department created me')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'thank you' in query:
            speak('you are welcome')

        elif 'play music' in query:
            speak('playing music')
            music="d:\\songs\\song01.mp3"
            os.startfile(music)

        elif 'open code' in query or 'chord' in query:
            speak('you are not authorised to make any changes or to view the code')
        
        elif 'shutdown' in query or 'power off' in query or 'Turn off' in query:

            if '2001' in query:
                speak('command accepted')
                speak('System Shutting Down')
                sys.exit()
            elif '2001' not in query:
                speak('Use Your authorisation code to shutdown')

        elif 'bella' in query or 'hi' in query or 'hello' in query:
            stMsgs = ['Hi', 'Hello', 'Whats up']

            speak(random.choice(stMsgs))

        elif 'appointment' in query:
            appointment()

        