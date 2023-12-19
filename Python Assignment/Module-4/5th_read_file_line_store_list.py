# Write a Python program to read a file line by line and store it into a list.

f=open("python.txt","r")

l=f.readlines()
l1=[]
for i in l:
    print(i)
    l1.append(i)

print(l1)