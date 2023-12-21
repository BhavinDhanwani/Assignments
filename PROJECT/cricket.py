import random
def batting():
    run=0
    for i in range(1,7):
        computer=random.randint(1,6)
        user=int(input("Choose between 1 to 6 :"))
        if user==computer:
            print("Wicket.")
            break
        elif user>6:
            print("Invalid Input.")
        else:
            print(f"You got {user} runs.")
            run+=user
    print("Your total score is :",run)
    return run
def balling():
    run1=0
    for i in range(1,7):
        user=int(input("Choose between 1 to 6 :"))
        computer=random.randint(1,6)
        if user==computer:
            print("Wicket.")
            break
        elif user>6:
            print("Invalid Input.")
        else:
            print(f"Computer made {computer} runs.")
            run1+=computer
    print(f"computer total score is {run1}")
    return run1
l1=["head","tail"]
name=input("Enter your name : ")
print("Welcome to Cricket ",name)
print("-----------------------------------")
match=input("Choose Head/Tail :").lower()

toss=random.choice(l1)
print("Toss result:",toss)
if toss==match:
    print("You won the toss.")
    choice=input("Choose Balling / Batting :").lower()
    if choice=="batting":
        run=batting()
        print("---------------Balling Turn---------------")
        run1=balling()
    elif choice=="balling":
        run1=balling()
        print("---------------Batting Turn---------------")
        run=batting()
    else:
        print("Incorrect Input.")
else:
    print("You lost the toss.")
    l2=["batting","balling"]
    choice=random.choice(l2)
    print("Computer wants ",choice)
    if choice=="balling":
        run1=balling()
        print("---------------Batting Turn---------------")
        run=batting()
    elif choice=="batting":
        run=batting()
        print("---------------Balling Turn---------------")
        run1=balling()

if run > run1:
    print(f"{name} wins the match")
elif run1 > run:
    print("Computer wins the match")
else:
    print("It's a tie!")