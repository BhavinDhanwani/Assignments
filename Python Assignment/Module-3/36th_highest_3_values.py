# Write a Python program to find the highest 3 values in a dictionary.

d={'A':60,'B':50,'c':30,'D':40,'E':10,'F':20}
l=list(d.values())
l=sorted(l)
print(l[-3:])