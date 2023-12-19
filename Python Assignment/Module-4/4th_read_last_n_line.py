# Write a Python program to read last n lines of a file.

f=open("python.txt","r")
n=int(input("Enter number of lines you want to read from last line : "))
reverse=f.readlines()
for i in range(1,n+1):
    print(reverse[-1])