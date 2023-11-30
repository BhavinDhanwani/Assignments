# Write a Python function to calculate the factorial of a number (a nonnegative integer)


def factorial(user):

    num=1
    for i in range(1,user+1):
            num=i*num
    print(f"factorial value of {user} is {num}")

user=int(input("enter any number to get the factorial: "))
factorial(user)