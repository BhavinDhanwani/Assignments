# Write a Python script to concatenate following dictionaries to create a new one.

d1={1:'Bhavin',2:'Dhanwani'}
d2={3:'Ashutosh',4:'Singh'}
d3={5:'Hello',6:'World'}
d4={}

for i in (d1,d2,d3):
    d4.update(i)

print(d4)