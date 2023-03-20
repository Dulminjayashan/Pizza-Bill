while True:
    print("        Welcome to ABC Pizza         ")
    print("Menu ")
    print("1.Vegi Pizza - Rs.400.00")
    print("2.Seafood Pizza - Rs.800.00")
    print("3.chicken Pizza - Rs.600.00")
    total=0
    total2=0
    total3=0

    #MENU
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            pizza = "Vegi Pizza"
            total= total+400.00
            break
        elif choice == '2':
            pizza = "Seafood Pizza"
            total= total+800.00      
            break
        elif choice == '3':
            pizza = "Chicken Pizza"
            total= total+600.00      
            break
        else:
            print("Invalid choice. Please try again.")
            
    #EXTRA ADDING
    print("Do you want something extra added?")
    extra = str(input("Enter YES or NO: ").upper())

    if extra == "YES":
        print("1. Extra cheese - Rs.100.00")
        print("2. Extra onions - Rs.40.00")
        print("3. Extra sauce - Rs.60.00")
       
        while True:
            extra = input("Enter your choice (1, 2, or 3): ")
            if extra == '1':
                extra = "Extra cheese"
                total2= total2+100.00
                break
            elif extra == '2':
                extra = "Extra onions"
                total2= total2+40.00
                break
            elif extra == '3':
                extra = "Extra sauce"
                total2= total2+60.00
                break
            else:
                print("Invalid choice. Please try again.")
        
    else:
        total2= 0.00
        print("No extras added.")
       
    #DRINKS
    print("Do you want some drinks?")
    drink = str(input("Enter YES or NO: ").upper())

    if drink == "YES":    
        print("What drink would you like?")
        print("1. Coke - Rs.200.00")
        print("2. Pepsi - Rs.200.00")
        print("3. Water - Rs.100.00")

        while True:
            drink = input("Enter your choice (1, 2, or 3): ")
            if drink == '1':
                drink = "Coke"
                total3= total3+200.00
                break
            elif drink == '2':
                drink = "Pepsi"
                total3= total3+200.00
                break
            elif drink == '3':
                drink = "Water"
                total3= total3+100.00
                break
            else:
                print("Invalid choice. Please try again.")
    else:
         total3= 0.00
         print("No Drinks.")
    #TP
    tp=total+total2+total3
         
    #BILL
    print(f"Your order: {pizza}")
    print(f"Added: {extra}")
    print(f"Drinks: {drink}")
    print("Total Price: ",str("Rs"),(tp))

    while True:
        a = input("Next Customer (Press Enter) ")
        break
        
