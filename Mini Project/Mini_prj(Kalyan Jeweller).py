# Kalyan Jewellers mini project.
print("\n")
print("--:-- WELCOME TO KALYAN JEWELLERS --:--")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
nm=input("Enter Your Name: ")
g=input("Enter 'F' for Female and 'M' for Male: ").upper()
a=int(input("Enter Age: "))

status=True # Initilization for entry validation loop.
fgt=0

while status:   # while loop for applying entry condition to run loop.

    print("---------------------------------------")
    prd=input("Enter Product: ")
    grm=int(input("Enter Product Gram: "))
    print("Current Gold Price (1 Grm): 5752")

    print("---------------------------------------")

    t=grm*5752  # Total Gold Rate
    print("Total Gold Rate: ",t)
    print("\n")
    print("Making Charges (1 Grm): 845")
    print("---------------------------------------")

    m=grm*845  # Total Making Charges
    print("Total Making Charges: ",m)
    print("\n")
    ta=t+m  # Total Amout Charges
    print("Total Amoutn: ",ta)
    print("-----------------------------------------------")

    dis=0
    if a>65 and g=='M': # Condition Statement applied for Male greater then 65 age.
        if ta>= 200000 and ta<= 300000: # If the purchase is between 2lac and 3lac.
            dis=ta*20/100   # Then the Discount will be 20%.
            print("You Got 20% Discount.")
        elif  ta>= 300000 and ta<= 500000:  # If the purchase is between 3lac and 5lac.
            dis=ta*30/100   # Then the Discount will be 30%.
            print("You Got 30% Discount.")
        elif ta>=500000:    # If the purchase is more then or equal to 5lac.
            dis=ta*35/100   # Then the Discount will be 35%.
            print("You Got 35% Discount.")
        else:
            print("No Discount For You")

    elif a<65 and g=='M' and a>0:   # Condition Statement applied for Male less then 65 age.
        if ta>= 200000 and ta<= 300000: # If the purchase is between 2lac and 3lac.
            dis=ta*10/100   # Then the Discount will be 10%.
            print("You Got 10% Discount.")
        elif  ta>= 300000 and ta<= 500000:  # If the purchase is between 3lac and 5lac.
            dis=ta*20/100   # Then the Discount will be 20%.
            print("You Got 20% Discount.")
        elif ta>= 500000:   # If the purchase is more then or equal to 5lac.
            dis=ta*25/100   # Then the Discount will be 25%.
            print("You Got 25% Discount.")
        else:
            print("No Discount For You.")

    elif a>65 and g=='F':   # Condition Statement applied for Female greater then 65 age.
        if ta>= 200000 and ta<= 300000: # If the purchase is between 2lac and 3lac.
            dis=ta*25/100   # Then the Discount will be 25%.
            print("You Got 25% Discount.")
        elif  ta>= 300000 and ta<= 500000:  # If the purchase is between 3lac and 5lac.
            dis=ta*35/100   # Then the Discount will be 35%.
            print("You Got 35% Discount.")
        elif ta>=500000:    # If the purchase is more then or equal to 5lac.
            dis=ta*40/100   # Then the Discount will be 40%.
            print("You Got 40% Discount.")
        else:
            print("No Discount For You")

    elif a<65 and g=='F' and a>0:   # Condition Statement applied for Female less then 65 age.
        if ta>= 200000 and ta<= 300000: # If the purchase is between 2lac and 3lac.
            dis=ta*15/100   # Then the Discount will be 15%.
            print("You Got 15% Discount.")
        elif  ta>= 300000 and ta<= 500000:  # If the purchase is between 3lac and 5lac.
            dis=ta*25/100   # Then the Discount will be 25%.
            print("You Got 25% Discount.")
        elif ta>= 500000:   # If the purchase is more then or equal to 5lac.
            dis=ta*30/100   # Then the Discount will be 30%.
            print("You Got 30% Discount.")
        else:
            print("No Discoount For You.")
    else:
        print("The given age is not proper.")

    print("Discout: ",dis)
    if dis>0:   
        print("Discount Amount Without Making Charges:",dis-m)
    else:   
        print("----------------------------------------------")

    tna=ta-dis  #Total net amount.
    print("Total Net Amout:",tna)
    print("\n")

    choice=input("If you want to purcase more then press 'Y' or else 'N'.").upper() # If the user wants to purchase more.
    if choice=='Y':
        status=True # If the condition is true then it will initilize while loop again.
    else:
        status=False    # It will break the loop.
        
    fgt+=tna    # Grand Total of all the products.

print("------------------------------------------------")
print("         Your Grand Total is:",fgt)
print("-:THANK YOU FOR VISITING KALYAN JEWELLERS:-")