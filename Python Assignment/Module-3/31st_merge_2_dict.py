# Write a Python script to merge two Python dictionaries.

d1={1:"one",2:"two"}
d2={3:"three",4:"four"}

d3=d1.copy()
d3.update(d2)
print(d3)