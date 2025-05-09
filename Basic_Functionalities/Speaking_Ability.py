import sys
import os

# Get the project root directory
project_root = os.path.abspath('D:/My Stuff/Programming/Projects/JARVIS')
sys.path.append(project_root)


import pyttsx3

engine=pyttsx3.init()    #initialising text to speech

def speak(text):    #text to speech function
    engine.say(text)
    engine.runAndWait()