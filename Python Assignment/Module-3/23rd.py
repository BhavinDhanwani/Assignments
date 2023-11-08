# Write a Python program to remove an empty tuple(s) from a list of tuples.

t=[(),("hello","world"),(),("Welcome","to"),(),("Python")]

for i in t:
    if i==():
        t.remove(i)
print(t)