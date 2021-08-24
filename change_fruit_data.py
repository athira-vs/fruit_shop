from var import *

def change_fruit_menu():
    print("\n\t_____CHANGE FRUIT DETAILS_____")
    print("\t1. Change fruit id")
    print("\t2. Change fruit name")
    print("\t3. Change fruit rate")
    print("\t4. Change imported from")
    print("\t5. Change import date")
    print("\t6. Change bought price")


def change_fruit_id():
    f_id = input("\n\tEnter the fruit id to be changed: ")

    # Filter out the fruit with corresponding f_id from fruit_obj_lst
    fruit_lst = list(filter(lambda a: a.f_id == f_id,fruit_obj_lst))

    #If a corresponding Fruits object is present in fruit_obj_lst
    if fruit_lst:
        new_f_id = input("\tEnter the new f_id: ")
        fruit_lst[0].set_f_id(new_f_id)  # Reset the corresponding f_id
    else:
        print("\t Fruit with f_id {} is not present.".format(f_id))


def change_fruit_name():
    f_id = input("\n\tEnter the fruit id: ")

    # Filter out the fruit with corresponding f_id from fruit_obj_lst
    fruit_lst = list(filter(lambda a: a.f_id == f_id,fruit_obj_lst))

    #If a corresponding Fruits object is present in fruit_obj_lst
    if fruit_lst:
        new_name = input("\tEnter the new name: ")
        fruit_lst[0].set_name(new_name)  # Reset the corresponding name
    else:
        print("\n\t Fruit with f_id {} is not present.".format(f_id))


def change_fruit_rate():
    f_id = input("\n\tEnter the fruit id: ")

    # Filter out the fruit with corresponding f_id from fruit_obj_lst
    fruit_lst = list(filter(lambda a: a.f_id == f_id,fruit_obj_lst))

    #If a corresponding Fruits object is present in fruit_obj_lst
    if fruit_lst:
        new_rate = input("\tEnter the new rate: ")
        fruit_lst[0].set_rate(new_rate)  # Reset the corresponding rate
    else:
        print("\n\t Fruit with f_id {} is not present.".format(f_id))


def change_imported_from():
    f_id = input("\n\tEnter the fruit id: ")

    # Filter out the fruit with corresponding f_id from fruit_obj_lst
    fruit_lst = list(filter(lambda a: a.f_id == f_id,fruit_obj_lst))

    #If a corresponding Fruits object is present in fruit_obj_lst
    if fruit_lst:
        new_imp_from = input("\tEnter the new value for import_from: ")
        fruit_lst[0].set_import_from(new_imp_from)  # Reset the corresponding import_from
    else:
        print("\n\t Fruit with f_id {} is not present.".format(f_id))


def change_import_date():
    f_id = input("\n\tEnter the fruit id: ")

    # Filter out the fruit with corresponding f_id from fruit_obj_lst
    fruit_lst = list(filter(lambda a: a.f_id == f_id,fruit_obj_lst))

    #If a corresponding Fruits object is present in fruit_obj_lst
    if fruit_lst:
        new_imp_date = input("\tEnter the new import date: ")
        fruit_lst[0].set_import_date(new_imp_date)  # Reset the corresponding import_date
    else:
        print("\n\t Fruit with f_id {} is not present.".format(f_id))


def change_buy_price():
    f_id = input("\n\tEnter the fruit id: ")

    # Filter out the fruit with corresponding f_id from fruit_obj_lst
    fruit_lst = list(filter(lambda a: a.f_id == f_id,fruit_obj_lst))

    #If a corresponding Fruits object is present in fruit_obj_lst
    if fruit_lst:
        new_buy_price = input("\tEnter the new buy price: ")
        fruit_lst[0].set_buy_price(new_buy_price)  # Reset the corresponding buy_price
    else:
        print("\n\t Fruit with f_id {} is not present.".format(f_id))


def change_fruit():

    change_fruit_menu()
    choice =  input("\n\tEnter your choice: ")

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


