# Write a Python program to sort three integers without using conditional statements and loops.

a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
c=int(input("Enter 3rd Number: "))

d=min(a,b,c)
e=max(a,b,c)
f=(a+b+c)-d-e

print(f"Sorted Integers : {d} {f} {e}")