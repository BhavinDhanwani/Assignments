# Write a Python function to check whether a number is in a given range

def test_range(n):
    if n in range(3,9):
        print(f" {n} is in the range")
    else :
        print("The number is outside the given range.")

# n=input("enter any number: ")
test_range(7)