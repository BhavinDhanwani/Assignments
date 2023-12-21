# Rock / Paper / Sissor Game.

import random

game_list =["rock","paper","scissor"]    # Creating List
status=True
while status:
    com = random.choice(game_list)
    user=input("Choose rock / paper / scissor:-").lower()
    if user==com:
        print("Tie.")
    elif user=="rock" and com=="scissor":
        print("You won the match.")
    elif user=="paper" and com=="rock":
        print("You won the match.")
    elif user=="scissor" and com=="paper":
        print("You won the match.")
    elif user=="rock" and com=="paper":
        print("You lost the match.")
    elif user=="paper" and com=="scissor":
        print("You lost the match.")
    elif user=="scissor" and com=="rock":
        print("You lost the match.")
    else:
        print("Invalid Input.")
    status=False
    break