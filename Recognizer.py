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
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print("Recognizer Error {0}".format(e))
        return None
    