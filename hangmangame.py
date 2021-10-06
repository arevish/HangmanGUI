import random
import string

from pygame.constants import KEYDOWN
from wordsvault import wordsare

def hangman():

    word = random.choice(wordsare).upper()
    # Neglecting words that have '- 'or 'space'
    while '-' in word or ' ' in word:
        word = random.choice(wordsare)
    # print(word)
    winturn = 0
    turns = 10 
    guessmade = ""
    valid_entry = set(string.ascii_uppercase)
    # valid entry "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while len(word)>0:
        main_word = ""
        
        for letter in word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "
        if main_word == word:
            print(main_word," \n Congrats, you guessed the word! YOU WIN!! ")
            print("You took ", winturn , "turns to win !")
            p = input("Press s to play again   ")
            if p == "s":
                hangman()
            break

        guess = input("guess the words \n"+ main_word  +"   ").upper()
        if guess in valid_entry:
            guessmade = guessmade + guess
            print(guessmade)
        else:
            print("Enter a valid characters ")
            continue
        if guess not in word:
            turns = turns - 1
            winturn +=1
            print(turns," turns left!" )
            if turns == 0 :
                print("GAME OVER!!, you ran out of tries. Maybe next time!")
                print("The word was ", word)
                p = input("Press s to play again    ")
                if p == "s":
                    hangman()
                quit()
print("Let's play hangman !!")
hangman()


