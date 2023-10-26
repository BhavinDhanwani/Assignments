# Write python program that swap two number with temp variable and without temp variable.

# 1. With temp variable.

print("Swapping two numbers with temp variable.")

a=10
b=20

temp=a
a=b
b=temp

print(a)
print(b)

# 2. Without temp variable.

print("Swaping two number without temp variable.")

a=15
b=30

a,b=b,a

print(a)
print(b)