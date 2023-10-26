# write a program to find simple interest.

print("Enter the values to find simple interest.")

a=int(input("Enter the Principal Amount:"))
b=int(input("Enter the Anual Rate (%):"))
c=int(input("Enter the Number of Years:"))
d=a*b*c/100

print("Your Principal amount is:",a)
print("Simple Interest is:",d)
print("Total Value is:",d+a)