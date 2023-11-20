# Write a Python function that takes two lists and returns true if they have at least one common member.

list1=[10,20,30,40,50,60,70]
list2=[20,50,80,90,100]

same_number=False       # creating new variable.

for items in list1:     
    if items in list2:
        same_number=True

if same_number:
    print("List 1 and List 2 have some common values.")
else:
    print("List 1 and List 2 do not have common values.")