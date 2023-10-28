# Write a Python program to remove duplicates from a list. 

list1=[10,10,20,30,30,40,50,50,60]      # creating list.

list2=set(list1)     # converting list into set.

list3=list(list2)        # converting set into list.

print("List with Duplicate values : ",list1)
print("List without Duplicate values : ",list3)