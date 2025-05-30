import speech_recognition as sr
import webbrowser
import pyttsx3
from googlesearch import search

import os
from dotenv import load_dotenv

from googleapiclient.discovery import build

load_dotenv() 

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()


youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def play_on_youtube(query):
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=query,
        type="video"
    )
    response = request.execute()
    
    if response["items"]:
        video_id = response["items"][0]["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        speak(f"Playing {query} on YouTube")
        webbrowser.open(video_url)
    else:
        speak("Sorry, I couldn't find any results.")
        
        
        
def searchfn(query):
        for url in search(query, num_results=1):
            webbrowser.open(url)
    
        
        
def processcommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open whatsapp" in c.lower():
        speak("opening whatsapp")
        webbrowser.open("https://web.whatsapp.com/")
  
       
        
    elif "play" in c.lower():
        query = c.lower().split("play", 1)[-1].strip()
        if query:
            play_on_youtube(query)
        else:
            speak("What would you like me to play?")
    else:
        
        searchfn(c)
        
    
    
    
if __name__ == "__main__":
    speak("INITIALIZATION COMPLETED")
    while True:
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)  
            print("\t\t\t\t")
            print("\t\t\t\t")
            print("\t\t\t\t")
            print("\t\t\t\t")
            print("\t\t\t\t")
            print("\t\t\t\t")
            print("\t\t\t\t")
            print("\t\t\t\t")
            print("\t\t\t\t")
            print("\t\t\t\t")
            print("Waiting For Command")
            print("\t\t\t\t")
            print("\t\t\t\t")
            print("\t\t\t\t")
            print("\t\t\t\t")
            audio = r.listen(source)

        try:
            
            command = r.recognize_google(audio)
            print(command)
            if(command.lower()=="jarvis"):
                speak("Welcome Sir") 
                speak("Waiting for Your command sir")
            elif "open" in command:
                processcommand(command)
            elif "play" in command:
                processcommand(command)
            
            elif "shut"in command:
                speak("Shutting Down")
                break
            else:
                speak("searching for"+command)
                processcommand(command)
                
                
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
