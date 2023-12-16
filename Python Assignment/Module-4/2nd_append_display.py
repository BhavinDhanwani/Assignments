# Write a Python program to append text to a file and display the text.

f=open("python.txt","a")
f.write("\nHello and welcome to python assignment.")
f=open("python.txt","r")
print(f.read())
f.close()