from var import *

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


def delete_fruit_by_name():
    name = input("Enter the fruit name to be deleted: ")
    fruit_present = False
    for f_id, fruit in fruit_dict.items():
        if fruit["name"] == name:                   # Fruit with given name is present
            del fruit_dict[f_id]                    # Delete fruit with the corresponding f_id
            fruit_present = True
            break
    if not fruit_present:
        print("\n\t" + name + " doesn't exist in database.")


def display_fruit_details():
    for f_id, fruit in fruit_dict.items():
        print("\n\tFruit id:\t{}".format(f_id))
        for key, value in fruit.items():
            print("\t{}:\t{}".format(key,value))








    

