# Write a Python program to test whether a passed letter is a vowel or not.

a=input("Enter any Alphabet:- ").lower()

if a in ["a","e","i","o","u"]:
    print(f"{a} is a Vowel.")
else:
    print(f"{a} is not a Vowel.")