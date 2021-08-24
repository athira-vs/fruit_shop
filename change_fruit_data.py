from var import *

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


def change_fruit():

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


