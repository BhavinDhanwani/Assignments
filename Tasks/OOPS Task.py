class Program:
    def fibbonacci(self):
        num=int(input("Enter Number to see Fibbonacci Series : "))
        a=0
        b=1

        print(a)
        print(b)

        for i in range(2,num):
            num=a+b
            print(num)
            a,b=b,num

    def factorial(self):
        a=int(input("Enter Any Number : "))
        f=1
        for i in range (1,a+1):
            f=f*i
        print(f"Factorial of {a} is {f}")

    def swap_number(self):
        a=int(input("Enter First number : "))
        b=int(input("Enter Second number : "))

        a,b=b,a
        print("First number : ",a)
        print("Second number : ",b)

menu=("""
        Menu
      1) Fibbonacci
      2) Factorial
      3) Swap Number
""")
obj=Program()
print(menu)
choice=int(input("Enter your choice : "))
if choice==1:
    obj.fibbonacci()
elif choice==2:
    obj.factorial()
elif choice==3:
    obj.swap_number()
else:
    print("Wrong Input.")