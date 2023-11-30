# Write a Python function to check whether a number is perfect or not.

def perfect(user):
    list1=[]
    for i in range(1,user):
        if user%i==0:
            list1.append(i)
        else:
            continue
        
    if sum(list1)==user:
            print(f"yes {user} is a prime number") 
    else:
        print("sorry this is not a prime number")

user=int(input("enter any number to check whether it is prime or not:"))
perfect(user)