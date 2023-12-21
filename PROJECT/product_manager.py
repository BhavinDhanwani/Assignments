#  product manager:

menu="""
        Menu
    press 1 for product manager
    press 2 for customer
"""
product={}  # Creating Blank Dictionary

flag=True
while flag:
    print(menu)
    choice=int(input("Enter Your Choice : "))
    status=True
    if choice==1:
        # product manager panel
        pass
        while status:
            specific_product={}
            product_name=input("Enter product name : ").lower()
            product_qty=int(input("Enter Qty : "))
            product_price=int(input("Enter product price of 1kg qty : "))

            if product_name in product:
                # fetch old qty from the dictionary.
                old_qty=product[product_name]['qty']
                specific_product['qty']=old_qty+product_qty
                specific_product['price']=product_price
            else:
                specific_product["qty"]=product_qty
                specific_product["price"]=product_price

            product[product_name]=specific_product

            print("Product = ",product)

            choice = input("Do you want to add more product : ").lower()
            if choice=='y' or choice=='yes':
                status=True
            else: 
                status=False
    elif choice==2:
        # customer panel
        print("\n ::::::: PRODUCT MENU ::::::: ")
        for k in product:
            print(f"{k} - 1kg price is RS. {product[k]['price']}")
            # print("~"*30)
        status=True
        cart={}
        while status:
            if product=={}:
                print("Sorry, No Products Available Right Now.")
                status=False
            else:
                prd=input("What do you want to buy? : ").lower()
                if prd in product:
                    prd = cart
                    print(cart)
                    qty=int(input("Enter quantity : "))
                    if qty in product_qty:
                        print("Stock out")
                    choice=input("Do you want something else? ").lower()
                    if choice=='y' or choice=='yes':
                        status=True
                    else:
                        status=False
                else:
                    print(f"{prd} is not available.")
    else:
        print("Invalid Input enter 1 or 2 only.")

    # not working properly have to work.