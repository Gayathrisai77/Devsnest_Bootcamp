  ###### SUPER MARKET #########
print("Name super market ")
print("A.PUSH\nB.PULL")
bill = 0
ans = input("Enter your choice:")
if ans=="A" or ans=="a":
    print("             WELCOME TO THE SUPERMARKET!!\n     Here is your trolley")
else:
    print("visit again! have a good day")
    
print("avaliable categories are below:")
def option1():
    print("food ")
def option2():
    print("fruits")
def option3():
    print("vegetables")
def option4():
    print("stationary")
def option5():
    print("home needs")
def option6():
    print("sports")
    
print("select the category you want to visit")
print("1.food")
print("2.fruits")
print("3.vegetables")
print("4.stationary")
print("5.home needs")
print("6.sports")


    
choice = input("Enter your choice:")
if choice=="1":
    option1()
if choice=="2":
    option2()
if choice=="3":
    option3()
if choice=="4":
    option4()
if choice=="5":
    option5()
if choice=="6":
    option6()
    
def home_needs():
    print("1.soaps:100/-")
    print("2.mats:200/-")
    print("3.boxes:150/-")
    print("4.bottles:100/-")
    print("5.chairs:300/-")
def sports_materials():
    print("1.shuttle cock:150/-")
    print("2.cricket bat:250/-")
    print("3.sports shoes:700/-")
    print("4.sports dress:1000")
    print("5.badminton set:500/-")
    
def food_court():
    print("1.pickels:200/-")
    print("2.dry fruits:400/-")
    print("3.chocalates:200/-")
    print("4.rice:500/-")
    print("5.oil:150/-")
    
def vegetables_court():
    print("1.tomato:80/-")
    print("2.onion:40/-")
    print("3.beet root:50/-")
    print("4.Green chills:60/-")
    print("5.carrot:30/-")
    
def stationary_material():
    print("1.pens:10/-")
    print("2.pencil box:20/-")
    print("3.Books:50/-")
    print("4.A-4 sheets:10/-")
    print("5.pouch:30/-")
    
def fruits_cat():
    print("1.Apples:100/-")
    print("2.Banana:70/-")
    print("3.Guava:50/-")
    print("4.pomagranate:50/-") 
    print("5.Grapes:40/-")



if choice=="5":
   print("Home Needs")
   home_needs()
def select_home_need(item_choice):
    global bill
    if item_choice == "1":
        print("You selected Soaps: 200/-")
        bill += 200
    elif item_choice == "2":
        print("You selected Mats: 500/-")
        bill += 500
    elif item_choice == "3":
        print("You selected Chairs: 300/-")
        bill += 300
    elif item_choice == "4":
        print("You selected Boxes: 250/-")
        bill += 250
    elif item_choice == "5":
        print("You selected Bottles: 500/-")
        bill += 500
    else:
        print("Invalid choice")

while True:
 choice = input("Enter the item number you want to purchase: (or) done to finish the shopping")
if choice.lower=="done":
 select_home_need(choice)
print("Your total bill is:", bill)

    
    
    
    
    
    
    
    
    
    




















