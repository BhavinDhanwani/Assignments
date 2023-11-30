# Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string. 
# Sample string: 'w3resource' 
# Expected output: 
# {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


myStr="w3resource"
myDict=dict()
for character in myStr:
    if character in myDict:
        myDict[character]+=1
    else:
        myDict[character]=1
print("The dictionary created from characters of the string is:")
print(myDict)