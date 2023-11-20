# Write a Python script to sort (ascending and descending) a dictionary by value.

dic={3:'welcome',2:'world',5:'python',4:'to',1:'Hello'}

print("Original",dic)
a=dict(sorted(dic.items()))
print("Ascending",a)
d=dict(sorted(dic.items(),reverse=True))
print("Descending",d)