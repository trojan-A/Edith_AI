# AI Virtual Assistant

import speech_recognition as sr
from time import ctime
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            Edith_Speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Edith_Speak("Sorry! I did not get that! Consider repeating..")
        except sr.RequestError:
            Edith_Speak("Sorry! My server is down  :(")
        return voice_data

def Edith_Speak(audio_string):
    tts  = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
        if 'what is your name' in voice_data:
            Edith_Speak("My name is Edith! Happy to help you!")
        if 'What time is it' in voice_data:
             Edith_Speak(ctime())
        if 'search' in voice_data:
             search = record_audio('what do yo want to search for?')
             url = 'https://google.co.in/search?q=' + search
             webbrowser.get().open(url)
             Edith_Speak("Here is what i found for " + search)
        if 'find location' in voice_data:
             location = record_audio("What is the Location?")
             url = 'https://google.nl/maps/place' + location + '/&amp;'
             webbrowser.get().open(url)
             Edith_Speak("Here is the location of " + location)
        if 'exit' in voice_data:
            Edith_Speak("Okay Sir! Exiting processes...")
            exit()
        if 'Edith' in voice_data:
            Edith_Speak("Yes sir! here at your service!")
        if 'Edith introduce yourself' in voice_data:
            Edith_Speak("Hello! This is Edith...A Personal AI Assistant of Aditya...How do i help you?")
        if 'Edith open google ' in voice_data:
            Edith_Speak("Okay! Opening google")
            url = 'https://google.co.in'
            webbrowser.get().open(url)



time.sleep(1)
Edith_Speak("Hello there..This is Edith, Your personal AI Assistant...How can I help you...")
while 1:
    voice_data = record_audio()
    respond(voice_data)
