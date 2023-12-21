print("Welcome to Amazing Pizza and Pasta Pizzeria.")
class A:
    menu=("""
            Menu
    Press 1 : Order Menu
    Press 2 : Exit
    """)
    def displayM(self):
        print(self.menu)
    menu1=("""
            ***   Pizza   ***

        (1) 1 Large pizza = 10.99 AUD
        (2) 2 Large pizza = 20.99 AUD
        (3) 3 Large pizza = 29.99 AUD
    ***Buy 4 or more pizza and get 1.5lt of softdrink free***
            
            ***   Pasta   ***
        
        (1) 1 Large pasta = 9.5 AUD
        (2) 2 Large pasta = 17.00 AUD
        (3) 3 Large pasta = 27.50 AUD
    ***Buy 4 or more pastas and get 2 bruschetta free***
            
    ***Buy 4 or more pizza and pasta and get 2 chocco brownie ice cream free***
    """)
    def displayM1(self):
        print(self.menu1)

status=True

while status:
    obj=A()
    obj.displayM()
    choice=int(input("Enter Your Choice : "))
    if choice==1:
        obj.displayM1()
        print("~"*80)
        name=input("Enter Your Name : ")
        print("Welcome To Amazing Pizza and Pasta Pizzeria : ",name)
        print("~"*65)
        pizza=int(input("Enter number of pizza you want : "))
        print("~"*60)
        if pizza==1:
            pizza_rate=10.99
            print("Your Pizza order amount is : ",pizza_rate)
        elif pizza==2:
            pizza_rate=20.99
            print("Your Pizza order amount is : ",pizza_rate)
        elif pizza==3:
            pizza_rate=29.99
            print("Your Pizza order amount is : ",pizza_rate)
        elif pizza==0:
            pizza_rate=0
            print("Your Pizza order amount is : ",pizza_rate)
        elif pizza>3:
            pizza_rate=pizza*10.99
            print("Your Pizza order amount is : ",pizza_rate)
            if pizza>=4:
                print("Congratulations!! you got 1.5lt of softdrink free.")
        print("-"*60)
        pasta=int(input("Enter number of pasta you want : "))
        print("~"*60)
        if pasta==1:
            pasta_rate=9.5
            print("Your Pasta order amount is : ",pasta_rate)
        elif pasta==2:
            pasta_rate=17.00
            print("Your Pasta order amount is : ",pasta_rate)
        elif pasta==3:
            pasta_rate=27.50
            print("Your Pasta order amount is : ",pasta_rate)
        elif pasta==0:
            pasta_rate=0
            print("Your Pasta order amount is : ",pasta_rate)
        elif pasta>3:
            pasta_rate=pasta*9.5
            print("Your Pasta order amount is : ",pasta_rate)
            if pasta>=4:
                print("Congratulations!! you got 2 bruschetta free.")
        else:
            status=True
        print("-"*60)                  
        print("::::::::::: Pizza and Pasta Bill :::::::::::")
        print(f"Bill for {name}")
        print("Your Pizza order amount is : ",pizza_rate)
        print("Your Pasta order amount is : ",pasta_rate)
        total=pizza_rate+pasta_rate
        print("Your Grand Total is : ",total)
        if pizza>=4:
                print("You got 1.5lt of softdrink free with this order.")
        if pasta>=4:
                print("You got 2 bruschetta free with this order.")
        if pizza>=4 and pasta>=4:
            print("You got 2 chocco brownie ice cream free with this order.")
        print("Thanks for your Oreder, Visit Again.")
        status=False
    else:
        status=False
        print("Menu Exited, Thanks for Visiting.")