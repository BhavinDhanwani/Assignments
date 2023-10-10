# Write a Python program to count the number of characters (character frequency) in a string.

string=input("Enter string to count characters: ")
count=0

for i in range(len(string)):

    if string[i] != ' ':
        count=count+1
    
print("total number of your string:",count)