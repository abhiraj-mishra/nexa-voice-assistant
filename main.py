import speech_recognition as sr
import webbrowser
import pyttsx3
import MusicLibrary
import requests
import time
import client
import os
from dotenv import load_dotenv
from gtts import gTTS
import pygame

# Load the environment variables from the .env file
load_dotenv()


print("nexa your personal voice assistant")

recognizer = sr.Recognizer()

newsapi = os.getenv("newsapi")


# use this sppeck funtion when offline

# def speech(text):
#     engine = pyttsx3.init()

#     # Get the current speaking rate (defaults to around 200 words per minute)
#     rate = engine.getProperty('rate')

#     # Set the new rate. You can experiment with different values.
#     # A value of 250-300 might sound more natural and faster.
#     new_rate = 250 
#     engine.setProperty('rate', new_rate)

#     # You can also change the voice to a female one if available
#     voices = engine.getProperty('voices')
#     # Use a loop to find a female voice
#     for voice in voices:
#         if voice.gender == 'female':
#             engine.setProperty('voice', voice.id)
#             break
    
#     engine.say(text)
#     engine.runAndWait()

#use this speech funtion when online

def speech(text):
    # Set lang to 'en-in' for Indian English and 'slow=False' for normal speed
    tts = gTTS(text, lang='en-in', slow=False) 
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # Unload and remove the temporary file
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def ProcessCommand(c):
    if "open google" in c.lower():
        webbrowser.open_new_tab("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open_new_tab("https://m.youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open_new_tab("https://www.facebook.com")
    elif "open linkdin" in c.lower():
        webbrowser.open_new_tab("https://www.linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = MusicLibrary.music[song]
        webbrowser.open_new_tab(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            # Extract the articles
            articles = data.get('articles', [])
            # Print the headlines
            for article in articles:
                speech(article['title'])
    else:
        #let gemini landle the request
        userword = c.lower()
        gemini_response = client.get_gemini_response(userword)
        print(f"Gemini Response: {gemini_response}")
        speech(gemini_response)





if __name__ == "__main__":
    speech("initializing nexa..")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("recognizing...")
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)

            word = recognizer.recognize_google(audio)
            if word.lower() == "nexa":
                # --- speak BEFORE touching mic again ---
                speech("hi, I am nexa")

                # now open mic again
                with sr.Microphone() as source:
                    print("nexa activated...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    ProcessCommand(command)

        except Exception as e:
            print("Error;", e)



# if __name__ == "__main__":
#     speech("initializing nexa..")
#     while True:
#         r = sr.Recognizer()
#         #listining for the wake word astra
#         #obtain audio from the microphone

#         print("recognizing...")
#         try:
#             with sr.Microphone() as source:
#                 print("Listining...")
#                 audio=r.listen(source, timeout=2, phrase_time_limit=2)
#             word = r.recognize_google(audio)
#             if (word.lower() == "nexa"):
#                 speech("hi, I am nexa")
#                 #listen for the command
#                 with sr.Microphone() as source:
#                     print("nexa activated...")
#                     audio=r.listen(source)
#                     command = r.recognize_google(audio)

#                     ProcessCommand(command)

#         except Exception as e:
#             print("Error; {0}".format(e))