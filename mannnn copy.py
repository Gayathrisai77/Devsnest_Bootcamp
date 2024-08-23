def welcome():
    print("Welcome to the Supermarket!")
    print("A.PUSH \n B.PULL")
    ans = input("Enter your choice:")
    if ans == "A" or ans == "a":
        print("          WELCOME TO THE SUPERMARKET\n             HERE IS YOUR TROLLEY")
def display_menu():
    print("Select the category you want to visit:")
    print("1. Food")
    print("2. Fruits")
    print("3. Vegetables")
    print("4. Stationary")
    print("5. Home Needs")
    print("6. Sports")
    print("7. Exit")

def display_food_items():
    print("Food Section:")
    print("1. Bread - 50/-")
    print("2. Milk - 30/-")
    print("3. Cheese -20/-")
    print("4. Eggs - 7/-")

def display_fruits_items():
    print("Fruits Section:")
    print("1. Apple - 100/-")
    print("2. Banana - 70/-")
    print("3. Orange - 40/-")
    print("4. Grapes - 50/-")

def display_vegetables_items():
    print("Vegetables Section:")
    print("1. Tomato - 40/-")
    print("2. Potato - 30/-")
    print("3. Onion - 40/-")
    print("4. Carrot - 20/-")

def display_stationary_items():
    print("Stationary Section:")
    print("1. Pen - 10/-")
    print("2. Pencil - 15/-")
    print("3. Notebook - 20/-")
    print("4. Eraser - 5/-")

def display_home_needs_items():
    print("Home Needs Section:")
    print("1. Soap - 20/-")
    print("2. Towel - 100/-")
    print("3. Shampoo - 50/-")
    print("4. Tissues - 100/-")

def display_sports_items():
    print("Sports Section:")
    print("1. Football - 150/-")
    print("2. Basketball - 200/-")
    print("3. Tennis Ball - 50/-")
    print("4. Yoga Mat - 300/-")

def display_bill(bill):
    print("Your total bill is: {}/-".format(bill))

def supermarket():
    bill = 0
    welcome()
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            display_food_items()
            item_choice = int(input("Enter the item number: "))
            if item_choice == 1:
                bill += 50
            elif item_choice == 2:
                bill += 30
            elif item_choice == 3:
                bill += 20
            elif item_choice == 4:
                bill += 7
            else:
                print("Invalid item number.")
        elif choice == "2":
            display_fruits_items()
            item_choice = int(input("Enter the item number: "))
            if item_choice == 1:
                bill += 100
            elif item_choice == 2:
                bill += 70
            elif item_choice == 3:
                bill += 40
            elif item_choice == 4:
                bill += 50
            else:
                print("Invalid item number.")
        elif choice == "3":
            display_vegetables_items()
            item_choice = int(input("Enter the item number: "))
            if item_choice == 1:
                bill += 40
            elif item_choice == 2:
                bill += 30
            elif item_choice == 3:
                bill += 40
            elif item_choice == 4:
                bill += 20
            else:
                print("Invalid item number.")
        elif choice == "4":
            display_stationary_items()
            item_choice = int(input("Enter the item number: "))
            if item_choice == 1:
                bill += 10
            elif item_choice == 2:
                bill += 15
            elif item_choice == 3:
                bill += 20
            elif item_choice == 4:
                bill += 5
            else:
                print("Invalid item number.")
        elif choice == "5":
            display_home_needs_items()
            item_choice = int(input("Enter the item number: "))
            if item_choice == 1:
                bill += 20
            elif item_choice == 2:
                bill += 100
            elif item_choice == 3:
                bill += 50
            elif item_choice == 4:
                bill += 100
            else:
                print("Invalid item number.")
        elif choice == "6":
            display_sports_items()
            item_choice = int(input("Enter the item number: "))
            if item_choice == 1:
                bill += 150
            elif item_choice == 2:
                bill += 200
            elif item_choice == 3:
                bill += 50
            elif item_choice == 4:
                bill += 300
            else:
                print("Invalid item number.")
        elif choice == "7":
            display_bill(bill)
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")

# Usage
supermarket()
