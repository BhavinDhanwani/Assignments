# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
d=a+b+c

if a==b & b==c & c==a:
    print ("Sum is Zero")

else:
    print("Your Sum is:",d)