# Write a python program to find the longest words.

f=open("python.txt","r")
l=f.read()
w=l.split()
largest_word=""

for i in w:
    wl=len(w)
    length=len(largest_word)
    if wl>length:
        largest_word=i
    elif wl==length:
        largest_word=largest_word+""+i

print("Longest word is :",largest_word)