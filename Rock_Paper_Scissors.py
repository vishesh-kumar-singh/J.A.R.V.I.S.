# This is the well known game of rock paper scissors made using random module.
# The user needs to choose between rock, paper and scissors and compete with the computer for the ultimate glory of rock paper scissors champion.

import random
from Speaking_Ability import speak
from Recognizer import ear

def play(entry):
    choice=["rock","paper","scissors"]

    computer=random.choice(choice)
    iuser=entry.lower()
    
    speak(f"I chose {computer}")

    if "rock" in iuser:
        user="rock"
    elif "paper" in iuser:
        user="paper"
    elif "scissors" in iuser:
        user="scissors"
    else:
        user="none"
    if computer==user:
        return "tie"
    elif computer=="rock" and user=="paper" or computer=="paper" and user=="scissors" or computer=="scissors" and user=="rock":
        return "user"
    elif user=="none":
        return "none"
    else:
        return "computer"
    
def play1():    
    user_score=0
    comp_score=0
    z=1
    while z<11:
        speak(f"what would you chose for round {z}")
        entry=ear()
        if entry is None:
            speak("Some error occured, please try again.")
            continue
        result=play(entry)
        if result=="tie":
            print("This round is a tie")
            speak("This round is a tie")
            user_score+=0
        elif result=="user":
            print("You won this round")
            speak("You won this round")
            user_score+=1
        elif result=="none":
            speak("invalid choice sir. Maybe you've miss spelled.")
            continue
        else:
            print("I won this round")
            speak("I won this round")                
            comp_score+=1
        z+=1
    print(f"Your Score: {user_score}\nMy Score: {comp_score}")
    if user_score>comp_score:
        speak(f"You got {user_score} points and I got {comp_score}, so you won the game")
    elif user_score<comp_score:
        speak(f"You got {user_score} points and I got {comp_score}, so I won the game, but you were a tough competition")
    else:
        speak(f"You got {user_score} and I got {comp_score}, so we had a tie")

    with open("score1.txt") as f:
        x=int(f.read())
        if user_score<=x:
            speak(f"by the way Your last highscore with which you won against me was {x}")
            print(f"Highscore: {x}")
        else:
            if user_score>comp_score:
                with open("score1.txt","w") as f:
                    speak(f"You also made a new highscore aginst me. Your last highscore with which you won against me was {x}")
                    print(f"New High-Score: {user_score}")
                    f.write(str(user_score))
            else:
                speak("You would have made a new highscore if I'd have scored less than you!")
                print(f"Highscore: {x}")