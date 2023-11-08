# Write a Python script to check if a given key already exists in a dictionary.

d={1:'Hello',2:'World'}

n=int(input("Enter key to check if it is available or not : "))

if n in d.keys():
    print("Available")
else:
    print("Not available.")