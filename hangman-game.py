import random

random_word=""
import hangman_words
# from hangman_words import word_list
lives=6
# Choose a random word

random_word+=random.choice(hangman_words.word_list)

num_letters=len(random_word)
guess=""
game_over=False
correct=[]

while not game_over:

# Check if the user input is correct or not
# Replace one of the blanks if its correct and loose a life if its incorrect
    display= ""
    for letter in random_word:
        if letter==guess:
            display+=letter
            correct.append(letter)
        elif letter in correct:
            display+=letter
        else:
            display+="_"
            
# Generate blank letters from the word and ask the User to guess a letter
    print(display)
    guess=input("Guess a letter:\n").lower()
    
# and repeat until...
# Check if all the banks are replaced or all the lives are lost, if yes Game Over!
    if guess not in random_word:
        lives-=1
        print(f"you guessed {guess}, that's not in the word.")
        print(f"you have {lives}/6 lives left")
    elif guess in correct:
            print(f"You have guessed letter {guess} before, try again!")
    if "_" not in display:
        game_over=True
        print("You Win.")
    elif lives==0:
        game_over=True
        print(f"The word was {random_word}\n You lose!!!")

