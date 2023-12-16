# Write a Python program to read last n lines of a file.

f=open("python.txt","r")
for i in f:
    print(f.readline()[-1:])