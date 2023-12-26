# Write a Python program to count the frequency of words in a file.

word =input("Enter a word you want to check frequency : ")
count = 0
with open("python.txt", 'r') as f: 
    for line in f: 
        words = line.split() 
        for i in words: 
            if(i==word): 
                count=count+1
print("Occurrences of the word", word, ":", count)