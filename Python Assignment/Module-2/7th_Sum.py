# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a=int(input("Enter 1st Value:- "))
b=int(input("Enter 2nd Value:- "))
c=int(input("Enter 3rd Value:- "))

if a==b or a==c or b==c:
    print("Two values are same so the sum is Zero.")
else:
    print("The sum is:-",a+b+c)