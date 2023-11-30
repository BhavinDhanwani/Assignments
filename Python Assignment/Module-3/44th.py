# Write a Python program to calculate the area of a trapezoid

# formula of trapezoid = ((a+b)/2)*h (h=hight)


print("enter values to calculate the area of a trapezoid:")

A=int(input("enter the value of A :"))
B=int(input("enter the value of B :"))
H=int(input("enter the value of H :"))

Trapezoid =round(((A+B)/2)*H ,3)  
print(f"Are of trapezoid = {Trapezoid}")