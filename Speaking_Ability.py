import pyttsx3

engine=pyttsx3.init()    #initialising text to speech

def speak(text):    #text to speech function
    engine.say(text)
    engine.runAndWait()