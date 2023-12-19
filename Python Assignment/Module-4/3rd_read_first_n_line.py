# Write a Python program to read first n lines of a file.

f=open("python.txt","r")
n=int(input("Enter number of lines you want to read from first line : "))
for i in range(1,n+1):
    print(f.readline())