# Write a Python program to count the occurrences of each word in a given sentence

sentence=input("enter a sentence:")

word=input("enter a word to count its occurence in  sentence:")

count=sentence.count(word)

print(f"{word} ocuurs {count} in the sentence")