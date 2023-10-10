# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

str1="Hello"
str2="Bhavin"

print(str1+" "+str2)

# print(str1[:2]+str2[-4:])
# print(str2[:2]+str1[-4:])

print(str1[:2]+str2[:2]+" "+str2[:2]+str1[:2])