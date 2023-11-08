# Write a Python program to unzip a list of tuples into individual lists.

t=[(1,'a'),(2,'b'),(3,'c')]

t1=[]
t2=[]
for i in t:
    t1.append(i[0])
    t2.append(i[1])
print(t1)
print(t2)