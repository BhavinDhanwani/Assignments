# Write a Python program to count occurrences of a substring in a string.

mainstring=input("enter main string:")
substring=input(("enter sub string:"))

count=mainstring.count(substring)

print(f"{mainstring} ocuurs {count} time in the string")