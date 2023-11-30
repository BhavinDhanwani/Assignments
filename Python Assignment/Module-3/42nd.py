# Write a Python function that checks whether a passed string is 
# palindrome or not

# if the reverse of the string is the same as the original string. 
# For example, "radar" and "level" are palindrome strings.

def palindrome():
    user=input("enter a string: ")
    list1=[]
    list2=[]
    for char in user:
        list1.append(char)
    for i in list1[::-1]:
        list2.append(i)       

    if list2==list1:
        print("yes it is a palindrome string")
    else:
        print("sorry it is not palindrome")
palindrome()