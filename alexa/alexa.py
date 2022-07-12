from datetime import datetime
from click import command
import speech_recognition as sr
import pyttsx3 as py
import pywhatkit as pw
import datetime
import wikipedia



listener = sr.Recognizer()
engine = py.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source,duration=1)
        print("say anything : ")
        audio= listener.listen(source)
        try:
            text = listener.recognize_google(audio)
            text = text.lower()
            if 'alexa' in text:
                text = text.replace('alexa','')
                 
            else:
                print("alexa hu mai ijjat se naam lekr bol")
        except:
            print("sorry, could not recognise")
        return text
def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace("play",'')
        talk('playing'+song)
        pw.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('current time is'+time)
    elif 'who is this' in command:
        person = command.replace('who is this','')
        info = wikipedia.summary(person,2)
        talk(info)
    else:
        print('please say the command again')
        
while True:
    run_alexa()