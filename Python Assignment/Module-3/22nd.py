# Write a Python program to find the repeated items of a tuple.

t=(1,2,3,4,5,6,1,3,5,4)

ui=set()
ri=[]

for i in t:
    if i in ui:
        if i not in ri:
            ri.append(i)
    else:
        ui.add(i)

print("Repeated items in the tuple : ",ri)