# Write a Python program to get the Factorial number of given number.

a=int(input("Enter any number:- "))
f=1

for i in range(1,a+1):
    f=f*i
print(f"Factorial of {a} is {f}")