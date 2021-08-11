fruit_rate = []

while True:
    print("\n\n_______MENU_______")
    print("1. Add Fruit")
    print("2. Delete Fruit")
    print("3. Search Fruit (By name)")
    print("4. Search Fruit (By Rate)")
    print("5. Change fruit name")
    print("6. Change fruit rate")
    print("7. Display fruits and Rates")
    print("8. Exit")
    
    ch = int(input("Enter your choice: "))
    if ch == 1:
        #Add Fruit
        fruit = input("Enter fruit name: ")
        rate = input("Enter the rate: ")
        fruit_rate.append([fruit,rate])
    elif ch == 2:
        #Delete Fruit
        fruit = input("Enter the fruit name to be deleted: ")
        #if fruit in fruit_rate:
        fruit_present = False
        for fruit_list in fruit_rate:
            if fruit_list[0] == fruit:
                fruit_rate.remove(fruit_list)
                fruit_present = True
                break
        if not fruit_present:
            print(fruit + " doesn't exist in database. Can't delete")
        
    elif ch == 3:
        #Search Fruit (By name)
        fruit = input("Enter the fruit name to be searched: ")
        fruit_present = False
        for fruit_list in fruit_rate:
            if fruit_list[0] == fruit:
                print("\n\nFruit: " + fruit_list[0] + " Rate: " + fruit_list[1])
                fruit_present = True
                break
        if not fruit_present:
            print("\n\n" + fruit + " doesn't exist in database.")
    elif ch == 4:
        #Search Fruit (By rate)
        rate = input("Enter the rate of fruits to be searched: ")
        fruit_present = False
        for fruit_list in fruit_rate:
            if fruit_list[1] == rate:
                print("\n\nFruit: " + fruit_list[0] + "  Rate: " + fruit_list[1])
                #print("Rate: " + fruit_list[1])
                fruit_present = True
                
        if not fruit_present:
            print("\n\nFruit doesn't exist with given rate in database.")


    elif ch == 5:
        #Change fruit name
        fruit = input("Enter the fruit name to be changed: ")
        fruit_present = False
        for fruit_list in fruit_rate:
            if fruit_list[0] == fruit:
                new_name = input("Enter the new name for fruit: ")
                fruit_list[0] = new_name
                fruit_present = True
                break
        if not fruit_present:
            print("\n\n" + fruit + " doesn't exist in database.")
    elif ch == 6:
        #Change fruit rate
        fruit = input("Enter the fruit for which rate is to be changed: ")
        fruit_present = False
        for fruit_list in fruit_rate:
            if fruit_list[0] == fruit:
                new_rate = input("Enter the new rate for fruit: ")
                fruit_list[1] = new_rate
                fruit_present = True
                break
        if not fruit_present:
            print("\n\n" + fruit + " doesn't exist in database.")

    elif ch == 7:
        #Display fruits and rates
        print("\n\nFruit\tRate")
        for fruit_list in fruit_rate:
            print(fruit_list[0] + "  " + fruit_list[1])
        #print(fruit_rate)
    elif ch == 8:
        #Exit
        break




    

