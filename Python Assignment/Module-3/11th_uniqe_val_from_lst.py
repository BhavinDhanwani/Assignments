# Write a Python program to get unique values from a list.

l1=[]

for i in range(1,6):
    n=int(input("Enter Values : "))
    l1.append(n)

print("Entered list which contain same value : ",l1)

l2 = set(l1)
l2 = list(l2)
print("List which can not contain same value : ",l2)