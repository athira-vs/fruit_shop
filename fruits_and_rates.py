from var import *

def add_fruit():
    f_id = input("\tEnter fruit id: ")
    name = input("\tEnter fruit name: ")
    rate = input("\tEnter the rate: ")
    import_from = input("\tEnter the place it is imported from: ")
    import_date = input("\tEnter the import date: ")
    buy_price = input("\tEnter the bought price: ")

    # Create a fruit object
    fruit = Fruits(f_id, name, rate, import_from, import_date, buy_price)

    # Add the new fruit object to the list
    fruit_obj_lst.append(fruit)
        

def delete_fruit():
    f_id = input("\n\tEnter the id of fruit to be deleted: ")

    # Filter out the fruit with corresponding f_id from fruit_obj_lst
    fruit_lst = list(filter(lambda a: a.f_id == f_id,fruit_obj_lst))

    #If a corresponding Fruits object is present in fruit_obj_lst
    if fruit_lst:
        fruit_obj_lst.remove(fruit_lst[0])  # Remove the corresponding Fruits object from the list
    else:
        print("\n\t Fruit with f_id {} is not present.".format(f_id))


def delete_fruit_by_name():
    name = input("\n\tEnter the fruit name to be deleted: ")

    # Filter out the fruit with corresponding name from fruit_obj_lst
    fruit_lst = list(filter(lambda a: a.name == name,fruit_obj_lst))

    #If a corresponding Fruits object is present in fruit_obj_lst
    if fruit_lst:
        fruit_obj_lst.remove(fruit_lst[0])  # Remove the corresponding Fruits object from the list
    else:
        print("\n\t Fruit with name {} is not present.".format(name))


# Prints all the attributes of each of the Fruits object present in fruit_lst
def display_fruit_details(fruit_lst):

    # For each fruit object in fruit_lst
    print("\n\tF_id | Name | Rate | Import From | Import Date | Buy Price")
    for fruit in fruit_lst:
        print("\t{} | {} | {} | {} | {} | {}".format(fruit.f_id, fruit.name, fruit.rate, fruit.import_from, fruit.import_date, fruit.buy_price)) 











    

