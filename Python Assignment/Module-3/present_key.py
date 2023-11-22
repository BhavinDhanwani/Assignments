# How Do You Check The Presence Of A Key In A Dictionary?

d={1:'a',2:'b',3:'c'}
k=int(input("Enter key to check if it present or not : "))

if k in d.keys():
    print("key is present.")
else:
    print("Key is not present.")