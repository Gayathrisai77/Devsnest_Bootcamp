#KAUN BANEGA CRORAPATI

print("welcome to kaun banega crorapati")
while True:
   print("\nThis is a game of luck and skill")
   print("what is your name")
   name = input("Enter your name:")
   print(f"welcome to KBC {name}")
   print("For the first question 100rs")

   bank = 0

   print("Q1.what is the capital of india?")
   print("A.delhi\nB.mumbai\nc.kolkata\nd.chennai")
   ans = input("Your answer:")
   if ans == "A" or ans == "a":
    print("correct answer! you won 100rs")
    bank += 100
   else:
    print("it's wrong answer")
    print("You lost the game")
    print("You won",bank,"rs")
    break
    
   print("Now We have 200rs question")
   print("Q2.How many players are there in a cricketteam?")
   print("A.11\nB.12\nc.13\nd.14")
   ans = input("Your answer:")
   if ans == "A" or ans == "a":
      print("correct answer! you won 200rs")
      bank += 200
   else:
      print("it's wrong answer")
      print("You lost the game")
      print("You won",bank,"rs")
      break
   print("Now we have 300rs question")
   print("Q3.Who is the prime minister of india?")
   print("A.Narendra modi\nB.rahul Gandi\nc.sonia gandi\nd.manmohan singh")
   ans = input("Your answer:")
   if ans == "A" or ans =="a":
      print("correct answer! you won 300rs")
      bank += 300
   else:
      print("it's wrong answer")
      print("You lost the game")
      print("You won",bank,"rs")
      break

   print("Now we have 800rs question")
   print("Q4.What company was originally call cadara?")
   print("A.apple\nB.amazon\nc.samsung\nd.flip cart")
   ans = input("Your answer:")
   if ans == "B" or ans =="b":
    print("correct answer! you won 500rs")
    bank += 800
   else:
    print("it's wrong answer")
    print("You lost the game")
    print("You won",bank,"rs")
    break

      
   print("Now we have 1000rs question")
   print("Q5.Which planet has the most moons?")
   print("A.earth\nB.venus\nc.mars\nd.saturn")
   ans = input("Your answer:")
   if ans == "D" or ans =="d":
    print("correct answer! you won 1000rs")
    bank += 1000
   else:
    print("it's wrong answer")
    print("You lost the game")
    print("You won",bank,"rs")
    break


   print("Now we have 1500rs question")
   print("Q5.How many heart does an octopus have?")
   print("A.6\nB.8\nc.3\nd.1")
   ans = input("Your answer:")
   if ans == "B" or ans =="b":
    print("correct answer! you won1500rs")
    bank += 1500
   else:
    print("it's wrong answer")
    print("You lost the game")
    print("You won",bank,"rs")
    break



  
      
      
    
    












