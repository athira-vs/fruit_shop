fruit_dict = {}
cart = []

def main_menu():
    print("\n\n_______MENU_______")
    print("1. Add fruit")
    print("2. Delete fruit")
    print("3. Search fruit")
    print("4. Change fruit details")
    print("5. Add to cart")
    print("6. Display fruits")
    print("7. Display cart")
    print("8. Exit")


def add_fruit():
    fr_id = input("\tEnter fruit id: ")
    name = input("\tEnter fruit name: ")
    rate = input("\tEnter the rate: ")
    import_from = input("\tEnter the place it is imported from: ")
    import_date = input("\tEnter the import date: ")
    buy_price = input("\tEnter the bought price: ")

    fruit_dict[fr_id]= {
        "name" : name,
        "rate" : rate,
        "imported_from" : import_from,
        "import_date" : import_date,
        "buy_price" : buy_price
        }

def delete_fruit():
    f_id = input("\tEnter the id of fruit to be deleted: ")
    #if fruit in fruit_dict:
    if f_id in fruit_dict.keys():
        del fruit_dict[f_id]
    else:
        print("\tInvalid fruit id. Can't delete")

def search_fruit_menu():
    print("\t____SEARCH FRUIT____")
    print("\t1. Search by name")
    print("\t2. Search by rate")

def search_fruit_by_name():
    name = input("Enter the fruit name to be searched: ")
    fruit_present = False
    for f_id, fruit in fruit_dict.items():
        if fruit["name"] == name:
            print("\n\tFruit id:\t{}".format(f_id))
            for key, value in fruit.items():
                print("\t{}:\t{}".format(key,value))
            fruit_present = True
    if not fruit_present:
        print("\n\t" + name + " doesn't exist in database.")

def search_fruit_by_rate():
    rate = input("Enter the fruit rate to be searched: ")
    fruit_present = False
    for f_id, fruit in fruit_dict.items():
        if fruit["rate"] == rate:
            print("\n\tFruit id:\t{}".format(f_id))
            for key, value in fruit.items():
                print("\t{}:\t{}".format(key,value))
            fruit_present = True
    if not fruit_present:
        print(f"\n\tFruit with rate {rate} doesn't exist in database.")
    
def display_cart():
    for fruit in cart:
        print("\n")
        for key, value in fruit.items():
            print("\t{}:\t{}".format(key,value))

def display_fruit_details():
    for f_id, fruit in fruit_dict.items():
        print("\n\tFruit id:\t{}".format(f_id))
        for key, value in fruit.items():
            print("\t{}:\t{}".format(key,value))

def add_to_cart():
    #List the fruits
    print("\n\tFRUIT ID\t|\tFRUIT NAME\t|\tFRUIT RATE")
    for f_id, fruit in fruit_dict.items():
        print("\t{}\t|\t{}\t|\t{}".format(f_id, fruit['name'], fruit['rate'] ))

    f_id = input("Enter the fruit id to add the item to cart: ")
    if f_id in fruit_dict.keys():
        cart.append(fruit_dict[f_id])
        #cart.append({"fr_id": f_id, "name" : fruit_dict[f_id]["name"], "rate" : fruit_dict[f_id]["rate"]})

def change_fruit_menu():
    print("\t_____CHANGE FRUIT DETAILS_____")
    print("\t1. Change fruit id")
    print("\t2. Change fruit name")
    print("\t3. Change fruit rate")
    print("\t4. Change imported from")
    print("\t5. Change import date")
    print("\t6. Change bought price")

def change_fruit_id():
    f_id = input("\tEnter the fruit id to be changed: ")
    if f_id in fruit_dict.keys():
        new_id = input("\tEnter new fruit id for {}: ".format(fruit_dict[f_id]['name']))
        fruit_dict[new_id] = fruit_dict[f_id] #Add the new entry
        del fruit_dict[f_id] #Delete the old entry
    else:
        print("\n\tInvalid fruit id")

def change_fruit_name():
    f_id = input("\tEnter the fruit id: ")
    if f_id in fruit_dict.keys():
        new_name = input("\tEnter the new name: ")
        fruit_dict[f_id]["name"] = new_name
    else:
        print("\n\tInvalid fruit id")

def change_fruit_rate():
    f_id = input("\tEnter the fruit id: ")
    if f_id in fruit_dict.keys():
        new_rate = input("\tEnter the new rate: ")
        fruit_dict[f_id]["rate"] = new_rate
    else:
        print("\n\tInvalid fruit id")

def change_imported_from():
    f_id = input("\tEnter the fruit id: ")
    if f_id in fruit_dict.keys():
        new_imp_frm = input("\tEnter the new value for imported from: ")
        fruit_dict[f_id]["imported_from"] = new_imp_frm
    else:
        print("\n\tInvalid fruit id")

def change_import_date():
    f_id = input("\tEnter the fruit id: ")
    if f_id in fruit_dict.keys():
        new_imp_date = input("\tEnter the new import date: ")
        fruit_dict[f_id]["import_date"] = new_imp_date
    else:
        print("\n\tInvalid fruit id")

def change_buy_price():
    f_id = input("\tEnter the fruit id: ")
    if f_id in fruit_dict.keys():
        new_price = input("\tEnter the new buy price: ")
        fruit_dict[f_id]["buy_price"] = new_price
    else:
        print("\n\tInvalid fruit id")

while True:
    main_menu()    
    ch = int(input("Enter your choice: "))
    if ch == 1:
        #Add Fruit
        add_fruit()
        
    elif ch == 2:
        #Delete Fruit
        delete_fruit() 

    elif ch == 3:
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
        change_fruit_menu()

        choice =  input("\tEnter your choice: ")

        if choice == '1':
            #Change fruit id
            change_fruit_id()

        elif choice == '2':
            #Change fruit name
            change_fruit_name()

        elif choice == '3':
            #Change fruit rate
            change_fruit_rate()

        elif choice == '4':
            #Change imported from
            change_imported_from()

        elif choice == '5':
            #Change import date
            change_import_date()

        elif choice == '6':
            #Change buy price
            change_buy_price()
        else:
            print("\n\tInvalid choice")

    elif ch == 5:
        #Add to cart
        add_to_cart()

    elif ch == 6:
        #Display fruit details
        display_fruit_details()

    elif ch == 7:
        #Display the cart
        display_cart()

    elif ch == 8:
        #Exit
        break
    else:
        print("\tInvalid Choice!!!")



    

