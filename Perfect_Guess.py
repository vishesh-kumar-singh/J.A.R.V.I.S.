import random
from Recognizer import ear
from Speaking_Ability import speak
choice=range(1,101)
comp=random.choice(choice)

def play():
    x=1
    speak("I chose my number. It's your turn to guess. All the best.")
    while True:
        entry=ear()
        if entry is None:
            speak("Some error occured, please try again.")
            continue
        else:
            iuser=entry.lower()
            user="none"
            for n in choice:
                if str(n) in iuser:
                    user=n
            if user=="none":
                speak("Last one was not clear, could you please repeat it for me?")
                continue
            elif user==comp:
                speak(f"You took {x} turns to guess! Still was fun playing this game with you!")
                print(f"Number of turns= {x}")
                break
            elif user>comp:
                speak("Smaller number please!")
                print("Smaller number required!")
                x+=1
            else:
                speak("Bigger number please!")
                print("Bigger number required!")
                x+=1
    with open("score2.txt") as f:
        y=int(f.read())
    if x < y:
        print(f"New High-Score: {x} Turns")
        print(f"Old High-Score: {y} Turns")
        speak(f"Congratulations! You've set a new high score with {x} turns! Your previous best score was {y} turns.")
        with open("score2.txt", "w") as f:
            f.write(str(x))
    elif x==y:
        speak(f"You managed to again reach your previous best score of {y} turns")
        print(f"High-Score: {y} Turns")
    else:
        speak(f"Your last best score was {y} turns.")
        print(f"High-Score: {y} Turns")


def play2():

    speak("Would you like me to clear the rules to you sir?")
    answer=ear()
    if answer is None:
        speak("Could you please repeat sir, that if you want to listen the rules?")
    elif "no" in answer or "not" in answer or "nope" in answer or "don't" in answer:
        play()
    else:
        speak("In this game I'll choose a number and you'll guess the number. I'll guide you by telling if the number is bigger or smaller")
        play()