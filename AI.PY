import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os     

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<=12:
        speak("Good morning  this is siri  how may i help you")
    elif hour>=12 and hour<=15:
        speak("good afternoon  this is siri  how may i help you")
    else:
        speak("Good evening  this is siri how may i help you")


def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognising...")
        query= recognizer.recognize_google(audio, language="en-in")
        print("user said :",query )
    except Exception as e:
        print("Say that again please....")
        speak("can you Say that again please....")
        return"none"
    return query

if __name__ == "__main__":
    wishMe()
while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak(results)
            print(results)
  
        elif "youtube" in query:
            webbrowser.open('youtube.com')
        
        elif "google" in query:
            webbrowser.open("google.com")

        elif "skills" in query:
            webbrowser.open("pwskill.com")
        
        elif "spotify" in query:
            webbrowser.open("spotify.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"dear the time is {strTime}")

        elif "voice" in query:
            if "female" in query:
                engine.setProperty('voice', voice[1].id)
            else:
                engine.setProperty('voice', voice[0].id)
        
            speak("hello dear i have swtched my voice how is it")

        elif "location" in query:
            speak("what is the location?")
            location = takeCommand()
            Url = ("https://www.google.com/maps"+ location)
            webbrowser.open(Url)
            speak("here is the location"+location)

            
        elif "let's talk " in query:
            speak("okay dear")

        elif "hello" in query:
            speak("hii dear")

        elif "how are you " in query:
            speak("i am fine what about you")

        elif "you doing" in query:
            speak("nothing special")
        
        elif "today's weather" in query:
            speak("yes it is ,i think today you can go for picnic")
        
        elif "thank you" in query:
            speak("welcome dear")

        elif "bye" in query:
            speak("bye dear ")
        

    


