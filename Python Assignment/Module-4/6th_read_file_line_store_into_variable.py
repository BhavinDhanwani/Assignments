# Write a Python program to read a file line by line store it into a variable.

f=open("python.txt","r")

l=f.readlines()
a=""
for i in l:
    a+=i

print(a)