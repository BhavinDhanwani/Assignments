# Write a Python program to check multiple keys exists in a dictionary.

d={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o'}

count=0
for k in d:
    count+=1

if count>1:    
    print(f"There are {count} keys present in the dictionary : (Multiple Keys are present)")    
else:
    print(f"There are {count} keys present in the dictionary : (Multiple Keys are not present)")    