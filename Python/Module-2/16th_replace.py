# Write a Python program to find the first appearance of the substring
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string.

str=input("Enter any string: ")

if "not poor" in str:
    str1=str.replace("not poor","good").lower()
    print(str1)
else:
    print(str)