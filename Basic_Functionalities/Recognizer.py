import sys
import os

# Get the project root directory
project_root = os.path.abspath('C:/My Stuff/Programming/Projects/JARVIS')
sys.path.append(project_root)

import speech_recognition as sr

recognizer = sr.Recognizer()    #initialising speech recognition

def ear():      #Speech recognition function
    with sr.Microphone() as source:
        print("listening...")
        try:
            audio = recognizer.listen(source)
            print("Recognising...")
            text = recognizer.recognize_google(audio)
            print("Recognized Text:", text)
            return text
        except TimeoutError:
            print("A timeout occurred. Please check your internet connection and try again.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print("Recognizer Error {0}".format(e))
        return None
    