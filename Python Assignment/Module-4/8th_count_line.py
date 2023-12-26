# Write a Python program to count the number of lines in a text file.

f=open("python.txt","r")
l=len(f.readlines())
print("The number of lines in a text file is :",l)