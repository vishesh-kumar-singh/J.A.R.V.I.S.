import webbrowser as web
import re
from Basic_Functionalities.Speaking_Ability import speak
from Basic_Functionalities.Recognizer import ear
from Games.Rock_Paper_Scissors import play1
from Games.Perfect_Guess import play2
from Basic_Functionalities.Brightness_and_Volume import set_brightness,set_volume,unmute, mute,switch_off,screen_saver,turn_off_monitor

speak("Initialising Jarvis")


while True:
    itext = ear()
    if itext is None:
        continue
    text=itext.lower()  # .lower() for case-insensitivity

    #exit functions
    if "goodbye jarvis" in text or "good bye jarvis" in text or text=="exit" or "Good night jarvis" in text:
        speak("Good Bye Sir!")
        break


    #fixed responses
    elif text=="hey jarvis":
        speak("Yes Sir!")
    elif text=="wake up daddy's home" or text=="wake up" or text=="daddy's home":
        speak("Welcome home sir!")
    elif text=="jarvis you are there" or text=="jarvis are you there":
        speak("at your service, sir")

    #opening Music
    elif ("open" in text or "mood" in text) and "imagine dragons" in text:
        speak("I'm opening your playlist containing best imagine Dragons songs sir. Hope you'll enjoy.")
        web.open("https://open.spotify.com/playlist/2jwrpkRfGbIcDTNiP9TVsZ")
    elif "open" in text and ("favourite" in text or "favourites" in text):
        speak("I'm opening a playlist based on your current favorites sir. Hope you'll enjoy.")
        web.open("https://open.spotify.com/playlist/2vZkZZCjIXAZicLEP2Nt57")
    elif ("open" in text or "mood" in text) and ("eminem" in text or "rap" in text):
        speak("I'm opening your playlist containing best eminem songs sir.")
        web.open("https://open.spotify.com/playlist/0khsRNhhHDewY4C4MeZ9vJ")
    elif ("open" in text and "spotify" in text)or("play" in text and "spotify" in text):
        speak("As you wish sir!! Hope you'll enjoy listening.")
        web.open("https://open.spotify.com")
    
    
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
        print(f"Noted-{note}")
    elif "clear" in text and ("notes" in text or "note" in text):
        with open("Notes.txt","w") as f:
            f.write("")
        speak(f"I have cleared all the notes")
        print(f"I noted down the following text: {note}")

    
    elif "brightness" in text:
        if 'maximum' in text or 'max' in text:
            level=100
        else:
            clean_text = re.sub(r"[^\w\s]", "", text)
            try:
                level = int([int(s) for s in clean_text.split() if s.isdigit()][0])
            except IndexError as ie:
                speak('Please provide a clear command!')
                print('Can\'t detect the level to change the brightness into.')
                continue
        set_brightness(level)

    elif "volume" in text:
        if 'maximum' in text or 'max' in text:
            level=100
        else:
            clean_text = re.sub(r"[^\w\s]", "", text)
            try:
                level = int([int(s) for s in clean_text.split() if s.isdigit()][0])
            except IndexError as ie:
                speak('Please provide a clear command!')
                print('Can\'t detect the level to change the volume into.')
                continue
        set_volume(level)
    elif 'unmute' in text:
        unmute()
    elif 'mute' in text:
        mute()

    elif 'screen' in text and 'off' in text:
        turn_off_monitor()
        continue

    elif "screen" in text and "saver" in text:
        screen_saver()

    elif "shut down" in text or "switch off" in text:
        speak("Are you Sure sir")
        Ctext = ear()
        if Ctext is None:
            continue
        text=Ctext.lower()
        speak("Are you Sure sir")
        if "yes" in text or "sure" in text:
            switch_off()