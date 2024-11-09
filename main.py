import webbrowser as web
from Speaking_Ability import speak
from Recognizer import ear
from Rock_Paper_Scissors import play1
from Perfect_Guess import play2

speak("Initialising Jarvis")


while True:
    itext = ear()
    if itext is None:
        continue
    text=itext.lower()  # Use .lower() for case-insensitivity

    #exit functions
    if "goodbye jarvis" in text or "good bye jarvis" in text or text=="exit" or "Good night jarvis" in text:
        speak("Good Bye Sir!")
        break
    elif text=="mute":
        break


    #fixed responses
    elif text=="hey jarvis":
        speak("Yes Sir!")
    elif text=="wake up daddy's home" or text=="wake up" or text=="daddy's home":
        speak("Welcome home sir!")
    elif text=="jarvis you are there" or text=="jarvis are you there":
        speak("at your service, sir")
    elif "introduce" in text and "yourself" in text:
        speak('''Hello, I'M JARVIS. I'm a companion of my master Vishesh Kumar Singh.
            I can handletasks like opening websites, opening files, opening spotify playlists, playing games like rock paper scissor and a perfect guess, on just voice command.
            I can note things down for you if you command me to do so.
            ''')
    elif "introduce" in text and ("me" in text or "master" in text or "daddy" in text):
        speak('''Hey, this is my master, Vishesh Kumar Singh, a fresher undergraduate at I.I.T. Kanpur, persuing bachelors degree in Mathematics and Scientific Computing''')


    #opening Music
    elif ("open" in text or "mood" in text) and "imagine dragons" in text:
        speak("I'm opening your playlist containing best imagine Dragons songs sir. Hope you'll enjoy.")
        web.open("https://open.spotify.com/playlist/2jwrpkRfGbIcDTNiP9TVsZ")
    elif "open" in text and ("favourite" in text or "favourites" in text):
        speak("I'm opening a playlist based on your current favorites sir. Hope you'll enjoy.")
        web.open("https://open.spotify.com/playlist/2vZkZZCjIXAZicLEP2Nt57")
    elif ("open" in text or "mood" in text) and ("emin" in text or "rap" in text):
        speak("I'm opening your playlist containing best eminem songs sir.")
        web.open("https://open.spotify.com/playlist/0khsRNhhHDewY4C4MeZ9vJ")
    elif ("open" in text and "spotify" in text)or("play" in text and "spotify" in text):
        speak("I'm opening your best playlist sir. Hope you'll enjoy listening.")
        web.open("https://open.spotify.com/playlist/4C3OKTdUNGLhvaVzsUaJ93")
    
    
    #opening Youtube and related
    elif "open" in text and "youtube" in text and "studio" in text:
        speak("Opening Youtube Studio!")
        web.open("https://studio.youtube.com/channel/UCrfHgB_DpacSY6vyWnfH8Yw")
    elif "open" in text and "youtube" in text and "channel" in text:
        speak("Opening your Youtube channel")
        web.open("https://youtube.com/@thevishesh16")
    elif "open" in text and "youtube" in text:
        speak("Opening Youtube!")
        web.open("https://youtube.com")

    
    #Opening other websites.
    elif "open" in text and "chat" in text and "gpt" in text:
        speak("opening chat-GPT")
        web.open("https://chatgpt.com")
    elif "open" in text and "github" in text:
        speak("opening Github")
        web.open("https://github.com")
    elif "open" in text and "linkedin" in text and "profile" in text:
        speak("opening your linkedin profile.")
        web.open("https://www.linkedin.com/in/thevishesh16/")
    elif "open" in text and "linkedin" in text:
        speak("opening linkedin")
        web.open("https://linkedin.com")
    elif "open" in text and "instagram" in text:
        speak("opening instagram")
        web.open("https://instagram.com")


    #opening System Files.
    elif "notes" in text and "linear" in text:
        speak("Opening notes on linear algebra by professor Arbind K Lal")
        web.open("file:///D:/Notes/MTH113M/MTH113M%20typed%20notes.pdf")
    elif "notes" in text and "single" in text and "calculus" in text:
        speak("Opening notes on single variable calculus")
        web.open("D:/Notes/MTH111M")

    
    #Games
    elif "play" in text and "rock" in text:
        play1()
    elif "play" in text and ("guess" in text or "gas" in text or "perfect" in text):
        play2()

    
    #Storing Data
    elif "note" in text and "that" in text:
        note=text.split("note that")[1]
        with open("Notes.txt","a") as f:
            f.write(f"-{note}\n")
        speak(f"I noted down the following text: {note}")
        print(f"I noted down the following text: {note}")
    elif "clear" in text and ("notes" in text or "note" in text):
        with open("Notes.txt","w") as f:
            f.write("")
        speak(f"I have cleared all the notes")
        print(f"I noted down the following text: {note}")