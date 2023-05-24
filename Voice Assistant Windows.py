import os
import speech_recognition as sr
import win32com.client as wcl
import webbrowser
import openai
# import pyttsx3
import datetime
# TODO: use pyttsx3 to make this program run in any platform
speaker = wcl.Dispatch('SAPI.SpVoice')


def say(text):
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print('Thinking...')
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return 'Some Error Occurred. Sorry'

# TODO: generate own ai and use it with this program to fully automate
if __name__ == '__main__':
    print('Welcome')
    say('Hello, I am Alfred, how may I help?')
    while True:
        print('Listening...')
        q1 = takeCommand()
        query1= q1.lower()
        # TODO: automate listening for sites
        sites = [['youtube', 'https://youtube.com'],['google', 'https://google.com'],['wikipedia', 'https://wikipedia.com'],['facebook', 'https://facebook.com'],]

        for site in sites:
            if f'Open {site[0]}'.lower() in query1:
                say(f'Opening {site[0]} sir...')
                webbrowser.open(site[1])

        if 'play music' in query1:
            # TODO: play any song
            musicPath = 'C:\songtest\song.mp3'
            os.system(f'{musicPath}')

        if 'the time' in query1:
            hour = datetime.datetime.now().strftime('%H')
            min = datetime.datetime.now().strftime('%M')
            m=int(min)
            h1=int(hour)

            if h1>12:
                h2=h1-12
                say(f'The time is {h2} {m} pm')
            elif h1==12 and  m==00:
                say(f'It is 12 noon')
            elif h1==12 and m!=00:
                say(f'The time is {h1} {m} pm')
            else:
                say(f'The time is {h1} {m} am')
        


        if 'bye bye' in query1:
            say("See you later! Thanks for talking to me...")
            break

b = input('Press Enter to exit...')
