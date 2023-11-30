# Write a Python program to convert degree to radian

# How do you convert degrees to radians formula?

# ---> multiply the number of degrees by π/180.

# How do you convert radians to degrees?

#---> multiply the number of radians by 180/π



user=int(input("enter any number to covert degree to radian: "))

Radian=round((user*3.14159265359)/180,3)  # round function will give me only three value after decimal point

print(Radian)