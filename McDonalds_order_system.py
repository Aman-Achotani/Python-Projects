print()
print("\t\t***Welcome to McDonalds***")
print()
name = input("Please enter your name : ")
menu_veg = {
    "1: Aloo Tikki Burger": 55,
    "2: Paneer Zinger Burger": 80,
    "3: Vegetable Tikki Burger": 90,
    "4: Fries": 50,
    "5: Aloo Strips": 75,
    "6: Veg Cheese Burger": 100,
}
menu_nonVeg = {
    "1: Chicken Zinger burger": 65,
    "2: Chicken Spicy Burger": 85,
    "3: Fish Burger": 100,
    "4: Meat Balls": 150,
    "5: Chicken nuggets": 75,
    "6: Non-Veg Cheese burger": 170,
    "7: Chicken Wrap": 100,
}
desert = {
    "1: Mocktail": 90,
    "2: Ice cream": 65,
    "3: Brownie": 90,
    "4: Choco lava cake": 100,
    "5: Fresh juice": 60,
    "6: Coke": 100,
    "7: Splash": 120,
}
veg_orders = []
nonVeg_orders = []
deserts_orders = []

while True:
    print(
        "For veg menu press 1 \nFor non-veg menu press 2 \nFor deserts and drinks press 3"
    )
    choose = input()

    if choose == "1":
        print(name, "choosed veg menu and items available are :")
        for items, price in menu_veg.items():
            print(items, ", Price is :", price)
        print()
        print(name, "please enter the key of the item you want to buy")
        item_choose = input()

        if item_choose == "1":
            print(
                name,
                "choosed : ",
                " Aloo Tikki Burger",
                "And price is :",
                menu_veg["1: Aloo Tikki Burger"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                veg_orders.append(" Aloo Tikki Burger")
                veg_orders.append("Price is")
                veg_orders.append(menu_veg["1: Aloo Tikki Burger"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "2":
            print(
                name,
                "choosed : ",
                " Paneer Zinger Burger",
                "And price is :",
                menu_veg["2: Paneer Zinger Burger"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                veg_orders.append(" Paneer Zinger Burger")
                veg_orders.append("Price is")
                veg_orders.append(menu_veg["2: Paneer Zinger Burger"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "3":
            print(
                name,
                "choosed : ",
                "  Vegetable Tikki Burger",
                "And price is :",
                menu_veg["3: Vegetable Tikki Burger"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                veg_orders.append(" Vegetable Tikki Burger")
                veg_orders.append("Price is")
                veg_orders.append(menu_veg["3: Vegetable Tikki Burger"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "4":
            print(name, "choosed : ", " Fries", "And price is :", menu_veg["4: Fries"])
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                veg_orders.append(" Fries")
                veg_orders.append("Price is")
                veg_orders.append(menu_veg["4: Fries"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "5":
            print(
                name,
                "choosed : ",
                "Aloo Strips ",
                "And price is :",
                menu_veg["5: Aloo Strips"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                veg_orders.append(" Aloo Strips")
                veg_orders.append("Price is")
                veg_orders.append(menu_veg["5: Aloo Strips"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "6":
            print(
                name,
                "choosed : ",
                " Veg Cheese Burger",
                "And price is :",
                menu_veg["6: Veg Cheese Burger"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                veg_orders.append(" Veg cheese Burger")
                veg_orders.append("Price is")
                veg_orders.append(menu_veg["6: Veg Cheese Burger"])

            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        else:
            print("Invalid input")

        ask_again = input("Want to buy more items(y/n):")
        if ask_again == "y":
            continue
        elif ask_again == "n":
            break
        else:
            print("Invalid input")

    if choose == "2":
        print(name, "choosed non-veg menu and items available are :")
        for items, price in menu_nonVeg.items():
            print(items, ", Price is :", price)
        print()
        print(name, "please enter the key of the item you want to buy")
        item_choose = input()

        if item_choose == "1":
            print(
                name,
                "choosed : ",
                " Chicken Zinger burger",
                "And price is :",
                menu_nonVeg["1: Chicken Zinger burger"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                nonVeg_orders.append(" Chicken Zinger burger")
                nonVeg_orders.append("Price is")
                nonVeg_orders.append(menu_nonVeg["1: Chicken Zinger burger"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "2":
            print(
                name,
                "choosed : ",
                " Chicken Spicy Burger",
                "And price is :",
                menu_nonVeg["2: Chicken Spicy Burger"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                nonVeg_orders.append(" Chicken Spicy Burger")
                nonVeg_orders.append("Price is")
                nonVeg_orders.append(menu_nonVeg["2: Chicken Spicy Burger"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "3":
            print(
                name,
                "choosed : ",
                "  Fish Burger",
                "And price is :",
                menu_nonVeg["3: Fish Burger"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                nonVeg_orders.append(" Fish Burger")
                nonVeg_orders.append("Price is")
                nonVeg_orders.append(menu_nonVeg["3: Fish Burger"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "4":
            print(
                name,
                "choosed : ",
                " Meat Balls",
                "And price is :",
                menu_nonVeg["4: Meat Balls"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                nonVeg_orders.append(" Meat Balls")
                nonVeg_orders.append("Price is")
                nonVeg_orders.append(menu_nonVeg["4: Meat Balls"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "5":
            print(
                name,
                "choosed : ",
                " Chicken nuggets",
                "And price is :",
                menu_nonVeg["5: Chicken nuggets"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                nonVeg_orders.append(" Chicken nuggets")
                nonVeg_orders.append("Price is")
                nonVeg_orders.append(menu_nonVeg["5: Chicken nuggets"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "6":
            print(
                name,
                "choosed : ",
                " Non-Veg Cheese burger",
                "And price is :",
                menu_nonVeg["6: Non-Veg Cheese burger"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                nonVeg_orders.append(" Non-Veg Cheese burger")
                nonVeg_orders.append("Price is")
                nonVeg_orders.append(menu_nonVeg["6: Non-Veg Cheese burger"])

            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

            ask_again = input("Want to buy more items(y/n):")
            if ask_again == "y":
                continue
            elif ask_again == "n":
                break

        elif item_choose == "7":
            print(
                name,
                "choosed : ",
                "  Chicken Wrap",
                "And price is :",
                menu_nonVeg["7: Chicken Wrap"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                nonVeg_orders.append("  Chicken Wrap")
                nonVeg_orders.append("Price is")
                nonVeg_orders.append(menu_nonVeg["7: Chicken Wrap"])

            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        else:
            print("Invalid input")

        ask_again = input("Want to buy more items(y/n):")
        if ask_again == "y":
            continue
        elif ask_again == "n":
            break
        else:
            print("Invalid input")

    if choose == "3":
        print(name, "choosed drinks and deserts menu and items available are :")
        for items, price in desert.items():
            print(items, ", Price is :", price)
        print()
        print(name, "please enter the key of the item you want to buy")
        item_choose = input()

        if item_choose == "1":
            print(
                name,
                "choosed : ",
                "  Mocktail",
                "And price is :",
                desert["1: Mocktail"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                deserts_orders.append(" Mocktail")
                deserts_orders.append("Price is")
                deserts_orders.append(desert["1:  Mocktail"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "2":
            print(
                name,
                "choosed : ",
                "Ice cream",
                "And price is :",
                desert["2: Ice cream"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                deserts_orders.append(" Ice cream")
                deserts_orders.append("Price is")
                deserts_orders.append(desert["2: Ice cream"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "3":
            print(
                name, "choosed : ", " Brownie ", "And price is :", desert["3: Brownie"]
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                deserts_orders.append(" Brownie")
                deserts_orders.append("Price is")
                deserts_orders.append(desert["3: Brownie"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "4":
            print(
                name,
                "choosed : ",
                " Choco lava cake",
                "And price is :",
                desert["4: Choco lava cake"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                deserts_orders.append(" Choco lava cake")
                deserts_orders.append("Price is")
                deserts_orders.append(desert["4: Choco lava cake"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "5":
            print(
                name,
                "choosed : ",
                " Fresh juice",
                "And price is :",
                desert["5: Fresh juice"],
            )
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                deserts_orders.append(" Fresh juice")
                deserts_orders.append("Price is")
                deserts_orders.append(desert["5: Fresh juice"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "6":
            print(name, "choosed : ", " Coke", "And price is :", desert["6: Coke"])
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                deserts_orders.append(" Coke")
                deserts_orders.append("Price is")
                deserts_orders.append(desert["6: Coke"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        elif item_choose == "7":
            print(name, "choosed : ", " Splash", "And price is :", desert["7: Splash"])
            print()
            proceed = input("Are you sure you want to buy this item(y/n): ")
            if proceed == "y":
                print("Item purchesed succesfully")
                deserts_orders.append(" Splash")
                deserts_orders.append("Price is")
                deserts_orders.append(desert["7: Splash"])
            elif proceed == "n":
                print("Item purchase denied")
                print("Thank you for visiting us!!!")

            else:
                print("Invalid input")

        ask_again = input("Want to buy more items(y/n):")
        if ask_again == "y":
            continue
        elif ask_again == "n":
            break
        else:
            print("Invalid input")


print()
print(name, "your total bill is : ", veg_orders + nonVeg_orders + deserts_orders)
print("Thank you", name, " visit us again !!!")
