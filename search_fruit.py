from var import *


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