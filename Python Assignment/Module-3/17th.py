# Write a Python program to check whether an element exists within a tuple.

t1=(1,2,3,4,5,6)
n=int(input("Enter number to check if it is available in tuple or not : "))

if n in t1:
    print(f"{n} is available in tuple.")
else:
    print(f"{n} is not available in tuple.")