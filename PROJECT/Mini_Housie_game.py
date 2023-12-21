# Housie game.
import random


print("----::---- WELCOME TO HOUSIE ----::----")
print("\n")
pl1=input("Enter Player 1 Name: ")
pl2=input("Enter Player 2 Name: ")
print("\n")
print(f"Welcome {pl1} & {pl2} in Housie Game.")
print("\n")
list=[]
for i in range(0,12):
    i=random.randint(0,101)
    list.append(i)
for no in list:
    print(no,end="  ")
print("\n")
start=input("Press Enter To Start.")
if start=="":
    l1=list[0:6]
    l2=list[6:12]
print(f"{pl1} = {l1}\n{pl2} = {l2}")
print("\n")

status=True
while status:
    pl=random.choice(list)
    print("Lucky Number is: ",pl)

    if pl in l1 and pl in l2:
        l1.remove(pl)
        l2.remove(pl)
        print(l1)
        print(l2)

    elif pl in l1:
        l1.remove(pl)
        print(l1)
        print(l2)
        if l1==[]:
            print(f"Congratulations {pl1} you won the game.")
            break

    elif pl in l2:
        l2.remove(pl)
        print(l1)
        print(l2)
        if l2==[]:
            print(f"Congratulations {pl2} you won the game.")
            break
    
    else:
        status=True
    
    

    choice=input("Press Enter.")
    if choice=="":
        status=True
    else:
        status=False
