from change_fruit_data import *
from fruits_and_rates import *
from search_fruit import *
from cart_and_bill import *


def main_menu():
    print("\n\n_______MENU_______")
    print("1. Add fruit")
    print("2. Delete fruit by name")
    print("3. Search fruit")
    print("4. Change fruit details")
    print("5. Display and buy")
    print("6. Display cart")
    print("7. Bill")
    print("8. Exit")


while True:
    main_menu()    
    ch = int(input("Enter your choice: "))
    if ch == 1:
        #Add Fruit
        add_fruit()
        
    elif ch == 2:
        #Delete Fruit
        delete_fruit_by_name() 

    elif ch == 3:
        #Search fruit
        search_fruit_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            #Search Fruit (By name)
            search_fruit_by_name()

        elif choice == '2':
            #Search Fruit (By rate)
            search_fruit_by_rate()
        else:
            print("Invalid Choice!!!")

    elif ch == 4:
        #Change fruit details
        change_fruit()
        
    elif ch == 5:
        #Display and buy
        display_and_buy()

    elif ch == 6:
        #Display cart
        display_cart()

    elif ch == 7:
        #Bill
        bill()
        
    elif ch == 8:
        #Exit
        break
    else:
        print("\tInvalid Choice!!!")