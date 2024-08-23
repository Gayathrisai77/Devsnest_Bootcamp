import random
word_list = ["believe","god","hard work","goals","patience"]
lives = 6
chosen_word = random.choice(word_list)
my_list = ["__"]*len(chosen_word)
print(my_list)
game_over=False
while not game_over:
    guessed_letter=input("Guess a leeter:").lower()
    for position in range(len(chosen_word)): #01234
        letter = chosen_word[position]
        if letter==guessed_letter:
          my_list[position]=guessed_letter
    print(my_list)
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("YOU LOOSE!")
    if "__" not in my_list:
        game_over=True
        print("YOU WIN!")
    if lives == 5:
           print("-----|------|")
           print("     0       ")        
    if lives == 4:
            print("----|------|")
            print("    0       ")             
            print("    |       ")     
                            
    if lives == 3:
            print("----|------|")
            print("    0       ")
            print("   /|       ")
                              
                              
    if lives == 2:
            print("----|------|")
            print("    0       ")
            print("   /|\      ")
                              
                              
    if lives == 1:
            print("----|------|")
            print("    0       ")     
            print("   /|\      ")
            print("   /        ")    
                              
    if lives == 0:
            print("----|------|")
            print("    0       ")          
            print("   /|\      ")
            print("   / \      ")    
 