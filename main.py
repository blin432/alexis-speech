import speech_recognition as sr
import webbrowser
import time
import os
import playsound
import random
from gtts import gTTS
from time import ctime


#initialize recongnizer  ( it is everyting for this library)
r = sr.Recognizer()

#using microphone
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            ben_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print("inside function")
            print(voice_data)
        except sr.UnknownValueError:
            ben_speak('Sorry, I did not get that')
        except sr.RequestError:
            ben_speak('Sorry, my spech service is down')
        return voice_data

#respond funciton
def respond(voice_data):
    if 'what is your name' in voice_data:
        ben_speak("my name is ben")
    if 'what time is it' in voice_data:
        ben_speak(ctime())
    if 'search' in voice_data:
        search = record_audio ('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        ben_speak('here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio ('what is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        ben_speak('here is the location of ' + location)    
    if 'exit' in voice_data:
        exit()


#funtion for alexa_speal
def ben_speak(audio_string):
    tts = gTTS(text =audio_string, lang = 'en' )
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


#time.sleep suspends execution for that amount of seconds
time.sleep(1)
ben_speak("how can I help you")
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)