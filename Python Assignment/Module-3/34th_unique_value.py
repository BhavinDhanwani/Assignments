# Write a Python program to print all unique values in a dictionary.

d={"A" : 1,"B" : 1,"C" : 2,"D" : 2,"E" : 3,"F" : 4}

print("Dictionary :",d)
a=set(d.values())
print("Unique Values :",a)