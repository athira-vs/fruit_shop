from var import *

def add_to_cart():
    #List the fruits
    print("\n\tFRUIT ID|FRUIT NAME|FRUIT RATE")
    for f_id, fruit in fruit_dict.items():
        print("\t{}\t|\t{}\t|\t{}".format(f_id, fruit['name'], fruit['rate'] ))

    f_id = input("Enter the fruit id to add the item to cart: ")
    if f_id in fruit_dict.keys():   # If fruit id exists
        if f_id in cart.keys():     # Item already in cart
            cart[f_id] += 1         # Increment the count of the fruit in cart 
        else:
            cart[f_id] = 1          # Add the fruit id to cart and initialise its count to 1



def delete_from_cart():
    display_cart()
    f_id = input("\tEnter the fruit id to be deleted from cart: ")
    if f_id in cart.keys():     # If the fruit id already exists in cart
        if cart[f_id] == 1:
            del cart[f_id]
        else:                   # Cart contains more than 1 quantity of the fruit
            cart[f_id] -= 1     # Decrement the count of the fruit
    else:
        print("\tInvalid fruit id. Doesn't exist in cart.")



def display_cart():
    print("\n\tFRUIT ID|FRUIT NAME|FRUIT RATE|QUANTITY")
    for f_id in cart.keys():
        print("\t{}\t|\t{}\t|\t{}\t|\t{}".format(f_id, fruit_dict[f_id]['name'], fruit_dict[f_id]['rate'], cart[f_id]))


def display_and_buy_menu():
    print("\t1. Add fruits to cart")
    print("\t2. Delete fruit from cart")
    print("\t3. Display cart")
    print("\t4. Bill")
    print("\t5. Go to previous menu")


def bill():
    print("\t"+"_"*15+"BILL"+"_"*15)
    #display_cart()
    total = 0
    print("\n\tFRUIT ID|FRUIT NAME|FRUIT RATE|QUANTITY|AMOUNT")
    for f_id in cart.keys():
        rate = fruit_dict[f_id]['rate']
        count = cart[f_id]
        amount = float(rate) * count
        total += amount
        print("\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}".format(f_id, fruit_dict[f_id]['name'], rate, count, amount))
    print("\t"+'*'*80)
    print("\tTOTAL AMOUNT:\t\t{}".format(total))


def display_and_buy():
    while True:
        display_and_buy_menu()
        ch = input("Enter your choice: ")
        if ch == '1':
            #Add fruits to cart
            add_to_cart()

        elif ch == '2':
            #Delete fruits from cart
            delete_from_cart()

        elif ch == '3':
            #Display cart
            display_cart()

        elif ch == '4':
            #Bill
            bill()

        elif ch == '5':
            #Exit
            break
        else:
            print("Invalid Choice!!!")
