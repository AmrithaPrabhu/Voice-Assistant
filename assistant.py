#importing what modules we need
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
import string
from zoneinfo import ZoneInfo
import pywhatkit as kit

#function to get the audio from the microphone
def speechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything: ")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Done")
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except:
        print("Sorry could not recognize what you said")
        exit()
    
#function to convert the text to speech
def textToSpeech(text):
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say(text)
    engine.runAndWait()

#main body of the program
if __name__=='__main__':
    myName=speechToText().lower()

    #the program starts only if the user says voice assistant's name, "sofa"
    if 'sofa' in myName:
          
        #starts
        textToSpeech("Hello, I am your personal assistant. How can I help you?")

        #main loop
        while True:

             data=speechToText()
             data=data.lower()

             #voice assistant name
             if "your name" in data:
               textToSpeech("My name is sofa")
            
            #opens youtube
             elif "youtube" in data:
                webbrowser.open("https://www.youtube.com/")
            
            #opens instagram
             elif "instagram" in data:
                webbrowser.open("https://www.instagram.com/")
            
            #opens twitter
             elif "twitter" in data:
               webbrowser.open("https://twitter.com/login")
           
            #opens reddit
             elif "reddit" in data:
               webbrowser.open("https://www.reddit.com/")
            
            #opens google
             elif "google" in data:
               webbrowser.open("https://www.google.com/")
            
            #opens amazon
             elif "amazon" in data:
              webbrowser.open("https://www.amazon.in/")
            
            #opens netflix
             elif "netflix" in data:
                webbrowser.open("https://www.netflix.com/")
            
            #tells joke
             elif "joke" in data:

               #joke in english
               if "english" in data:
                textToSpeech(pyjokes.get_joke(language="en",category='neutral'))
            
               #joke in german
               elif "german" in data:
                textToSpeech(pyjokes.get_joke(language='de'))
               
               #joke in spanish
               elif "spanish" in data:
                textToSpeech(pyjokes.get_joke(language='es'))
          
             #date right now
             elif "date" in data:
                date=datetime.datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime("%d/%m/%Y")
                textToSpeech("Today is" + date)

             #time right now   
             elif "time" in data:
                time=datetime.datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime("%H:%M:%p")
                textToSpeech("The time is" + time)

             #exits the program   
             elif "exit" in data:
                textToSpeech("Have a great day!")
                exit()
            
             #gives the google search result of the same
             else:
                kit.search(data)

    #exits the program if the user doesn't say "sofa"   
    else:
        textToSpeech("Invalid Instruction")
        exit()


