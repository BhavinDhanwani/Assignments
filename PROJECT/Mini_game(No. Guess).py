# Number Guessing Game.

import random   # Importing random Module

status=True
com=random.randint(1,10)    # Computer will guess the number between 1 to 10.
com1=random.randint(1,15)    # Computer will guess the number between 1 to 15.
com2=random.randint(1,20)    # Computer will guess the number between 1 to 20.

print("--:-- WELCOME TO NUMBER GUESSING GAME --:--")
print("\n-----------Welcome to First Level----------\n")
user=0
user1=0
user2=0
while status:   # Initilizating entry level loop.

        for i in range(1,6):
             
            user=int(input("Enter your guess:- "))   # Get the user input 

            if user>com:    # If the user guess is upper then computer.
                print("Guess Lower Number.")    # Will print this.
            elif user<com:  # If the user guess is lower then computer.
                print("Guess Upper Number.")    # Will print this.
            else:
                print("Correct Answer.")    # Will print this.
                print("Congrulations!!! You Won the First Level.")
                result1=20
                print("\n-----------Welcome to Second Level----------\n")
                status=False
                for j in range (1,4):
                     
                    user1=int(input("Enter your guess:- "))
                    if user1>com1:  # If the user guess is upper then computer.
                        print("Guess Lower Number.")  # Will print this.
                    elif user1<com1:    # If the user guess is lower then computer.
                        print("Guess Upper Number.")  # Will print this.
                    else:
                        print("Correct Answer.")    # Will print this.
                        print("Congrulations!!! You Won Second Level.")
                        result2=30
                        result2+=result1
                        print("\n-----------Welcome to Third Level----------\n")
                        status=False
                        for k in range (1,3):

                            user2=int(input("Enter your guess:- "))
                            if user2>com2:   # If the user guess is upper then computer.
                                print("Guess Lower Number.")    # Will print this.
                            elif user2<com2: # If the user guess is lower then computer.

                                print("Guess Upper Number.")    # Will print this.
                            else:
                                print("Correct Answer.")    # Will print this.
                                print("Congrulations!!! You Won The Game.")
                                result3=50
                                result3+=result2
                                print("Game Over Thank You For Playing.")
                                status=False
                                break
                        
                        break   # Used to break 3rd for loop.
                    
                break   # Used to break 2nd for loop.
        
        break   # Used to break 1st for loop.

if user!=com:
    power=input("Do you want to use power and see the correct answer then enter 'Y'").upper()
    if power=='Y':
        print("Correct Answer is:",com)
        # status=True
    else:
        print("You Lost The Game.")
else:
    # break


 if user1!=com1:
    power=input("Do you want to use power and see the correct answer then enter 'Y'").upper()
    if power=='Y':
        print("Correct Answer is:",com1)
        # status=True
    else:
        print("You Lost The Game.")
 else:
    # print(" ")

  if user2!=com2:
    power=input("Do you want to use power and see the correct answer then enter 'Y' : ").upper()
    if power=='Y':
        print("Correct Answer is:",com2)
        # status=True
    else:
        print("You Lost The Game.")
  
  else:
    print(" ")
print("No More Chance Available.")

print("\n-------------------------------\n")

if user2==com2:
    print(f"You Got {result3} Points in this Game.")
elif user1==com1:
    print(f"You Got {result2} Points in this Game.")
elif user==com:
    print(f"You got {result1} Points in this Game.")
else:
    print("Game Over.")
