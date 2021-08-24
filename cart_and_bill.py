from var import *

def add_to_cart():
    #List the fruits
    print("\n\tF_id | Name | Rate")
    for fruit in fruit_obj_lst:
        print("\t{} | {} | {}".format(fruit.f_id, fruit.name, fruit.rate)) 

    f_id = input("\n\tEnter the fruit id to add the item to cart: ")

    # Filter out the fruit with corresponding f_id from fruit_obj_lst
    fruit_lst = list(filter(lambda a: a.f_id == f_id,fruit_obj_lst))

    #If a corresponding Fruits object is present in fruit_obj_lst. i.e. if fruit id exists
    if fruit_lst:

        if f_id in cart.keys():     # Item already in cart
            cart[f_id] += 1         # Increment the count of the fruit in cart 
        else:
            cart[f_id] = 1          # Add the fruit id to cart and initialise its count to 1



def delete_from_cart():
    display_cart()
    f_id = input("\n\tEnter the fruit id to be deleted from cart: ")
    if f_id in cart.keys():     # If the fruit id already exists in cart
        if cart[f_id] == 1:
            del cart[f_id]
        else:                   # Cart contains more than 1 quantity of the fruit
            cart[f_id] -= 1     # Decrement the count of the fruit
    else:
        print("\n\tInvalid fruit id. Doesn't exist in cart.")



def display_cart():
    print("\n\tFRUIT ID|FRUIT NAME|FRUIT RATE|QUANTITY")
    for f_id in cart.keys():
        # Filter out the fruit with corresponding f_id from fruit_obj_lst
        fruit_lst = list(filter(lambda a: a.f_id == f_id,fruit_obj_lst))

        #If a corresponding Fruits object is present in fruit_obj_lst. i.e. if fruit id exists
        if fruit_lst:
            print("\t{}\t|\t{}\t|\t{}\t|\t{}".format(f_id, fruit_lst[0].name, fruit_lst[0].rate, cart[f_id]))


def display_and_buy_menu():
    print("\n\t1. Add fruits to cart")
    print("\t2. Delete fruit from cart")
    print("\t3. Display cart")
    print("\t4. Bill")
    print("\t5. Go to previous menu")


def bill():
    print("\n\t"+"_"*15+"BILL"+"_"*15)
    #display_cart()
    total = 0
    print("\n\tFRUIT ID|FRUIT NAME|FRUIT RATE|QUANTITY|AMOUNT")
    for f_id in cart.keys():

        # Filter out the fruit with corresponding f_id from fruit_obj_lst
        fruit_lst = list(filter(lambda a: a.f_id == f_id,fruit_obj_lst))

        #If a corresponding Fruits object is present in fruit_obj_lst. i.e. if fruit id exists
        if fruit_lst:
            rate = fruit_lst[0].rate
            count = cart[f_id]
            amount = float(rate) * count
            total += amount
            print("\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}".format(f_id, fruit_lst[0].name, rate, count, amount))
    print("\t"+'*'*80)
    print("\tTOTAL AMOUNT:\t\t{}".format(total))


def display_and_buy():
    while True:
        display_and_buy_menu()
        ch = input("\n\tEnter your choice: ")
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
            print("\n\tInvalid Choice!!!")
