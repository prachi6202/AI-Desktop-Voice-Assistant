import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wk
import webbrowser
import os
#import PyAudio



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("i am enaa. please tell me how may i help you")



def takecommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold =1
        audio=r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query= query.replace("wikipedia","")
            results=wk.summary(query,sentences=4)
            speak("according to wikipedia....")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir= "specify the path"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            strftime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{strftime}")

        elif "quit" in query:
            exit()
