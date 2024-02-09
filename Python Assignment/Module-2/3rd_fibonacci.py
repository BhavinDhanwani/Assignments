# Write a Python program to get the Fibonacci series of given range.

num=int(input("Enter any number to see fibonacci series : "))
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    num=a+b
    print(num)
    a,b=b,num