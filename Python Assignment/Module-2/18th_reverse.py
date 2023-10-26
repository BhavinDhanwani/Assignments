# Write a Python function to reverses a string if its length is a multiple of 4.

a=input("Enter any word: ")

if len(a)%4==0:
    for i in a[::-1]:
        print(i,end="")
else:
    print("This word can not reverse because it is not multiple of 4.")