# Write a Python program to add 'ing' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then add
# 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

str=input("Enter any string.")

print(len(str))

if len(str)>=3 and str.endswith("ing"):
    print(str+"ly")
elif len(str)>=3:
    print(str+"ing")
else:
    print(str)