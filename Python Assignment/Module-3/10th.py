# Write a Python program to find the second smallest number in a list. 

list=[10,20,30,50,60,80,90]

smallest=min(list)
list.remove(smallest)
smallest1=min(list)
print(smallest1)