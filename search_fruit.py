from var import *
#from fruits_and_rates import *
from fruits_and_rates import display_fruit_details


def search_fruit_menu():
    print("\n\t____SEARCH FRUIT____")
    print("\t1. Search by name")
    print("\t2. Search by rate")

def search_fruit_by_name():
    name = input("\n\tEnter the fruit name to be searched: ")

    # Filter out the fruit with corresponding name from fruit_obj_lst
    fruit_lst = list(filter(lambda a: a.name == name,fruit_obj_lst))

    #If a corresponding Fruits object is present in fruit_obj_lst, display its details.
    if fruit_lst:
        display_fruit_details(fruit_lst)
    else:
        print("\n\t Fruit with name {} is not present.".format(name))


def search_fruit_by_rate():
    rate = input("\n\tEnter the fruit rate to be searched: ")

    # Filter out the fruit with corresponding rate from fruit_obj_lst
    fruit_lst = list(filter(lambda a: a.rate == rate,fruit_obj_lst))

    #If a corresponding Fruits object is present in fruit_obj_lst, display its details.
    if fruit_lst:
        display_fruit_details(fruit_lst)
    else:
        print("\n\t Fruit with name {} is not present.".format(name))