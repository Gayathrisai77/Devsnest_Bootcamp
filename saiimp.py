name = input("what is your name?")      #here we are welcoming user 
print("Hello,"+name,"lets play the game!")  #here printing the hello with giving user name
print("start guessing....")#here we are printing some stmnts to start game
words = ["sucess","dream","goal","god","belive"]
import random
word = random.choice (words)
print(word)
guesses = ""    #creating a variable with empty values
turns = 10      # no.of turns has to given
# create a while loop
# check if the turns more than zero 
while turns > 0: 
    #make a counter that starts with zero,#count the no.of times a user fails
  failed = 0
  #for every character in dream word
  for str in word:
      #see if the character is in the players guess
    if str in guesses:
        #print then out the caracter
      print(str,end="")
    else:
        #if not found,print a dash
        print("_",end="")
        #and increase the failed counter with one 
        failed += 1
        #if failed is equal to zero
        #user will win the game if failure is 0
  if failed == 0:
      print( "YOU WON THE GAME")
      #this print the correct word
      print("The word is: ", word)
      break
  #if user has input the wrong alphabet it will ask user to enter another one 
  guess = input("guess a character:")
  #every input character will be stored in guesses
  guesses += guess
  #check the input with the character in word
  if guess not in word:
        turns -= 1
        #if the character doesnot match the word then "wrong"will given as output
        print("wrong")
        #this will print the no.of turns left for the user
        print("YOU HAVE ",+turns,"more guesses")
        if turns == 9:
           print("-----|------|")
           print("     0       ")        
        if turns == 8:
            print("----|------|")
            print("    0       ")             
            print("    |       ")     
                            
        if turns == 7:
            print("----|------|")
            print("    0       ")
            print("   /|       ")
                              
                              
        if turns == 6:
            print("----|------|")
            print("    0       ")
            print("   /|\      ")
                              
                              
        if turns == 5:
            print("----|------|")
            print("    0       ")     
            print("   /|\      ")
            print("   /        ")    
                              
        if turns == 4:
            print("----|------|")
            print("    0       ")          
            print("   /|\      ")
            print("   / \      ")    
                              
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                              
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  if turns == 0:
     print("YOU LOST THE GAME")