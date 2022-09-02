import random
import re
from players import player_list_hard, player_list_easy, player_list_medium

def get_player_hard():
    word = random.choice(player_list_hard)
    return word.upper()

def get_player_easy():
    word = random.choice(player_list_easy)
    return word.upper()

def get_player_medium():
    word = random.choice(player_list_medium)
    return word.upper()

def play(word):
    word_completion = word
    for letter in word_completion:
        if letter.isalpha():
            word_completion = word_completion.replace(letter, "_")
    guessed = False
    guessed_letters = []
    guessed_words = []
    hint_total = 0
    tries = 6
    print("Let's play HangFooty!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or a word(enter '?' for a hint): ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter")
            elif guess not in word:
                print(guess, "is not in the players name")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the name!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already gessed the letter", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        elif guess == "?":
            for letter in word:
                if hint_total == 3:
                    print('MAX HINTS REACHED')
                    break
                elif letter not in word_completion:
                    word_completion = re.sub("_", letter, word_completion, 1)
                    hint_total = hint_total + 1
                    break     
        else:
            print("Not a valid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the player! You win!")
        while input("Play Again? (Y/N) ").upper() == "Y":
            main()
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")    



def display_hangman(tries):
    stages = [ """ 
                        --------
                        |      |
                        |      0  
                        |     \\|/
                        |      |
                        |     / \\ 
                        -
                    """,
                    """
                        ---------
                        |       |
                        |       0    
                        |      \\|/
                        |       |
                        |      /
                        -
                    """,
                    """

                        ---------
                        |       |
                        |       0    
                        |      \\|/
                        |       |
                        |      
                        -
                    """,
                    """

                        ---------
                        |       |
                        |       0    
                        |      \\|
                        |       |
                        |      
                        -
                    """,
                    """

                        ---------
                        |       |
                        |       0    
                        |       |
                        |       |
                        |      
                        -
                    """,
                    """

                        ---------
                        |       |
                        |       0    
                        |       
                        |       
                        |      
                        -
                    """,
                    """

                        ---------
                        |       |
                        |          
                        |       
                        |       
                        |      
                        -
                    """
    ]
    return stages[tries]

def main():
    x = input("Choose difficulty: E/M/H ").upper()
    if x == "E":
        word = get_player_easy()
        play(word)
            
    elif x == "M":
        word = get_player_medium()
        play(word)
            
    elif x == "H":
        word = get_player_hard()
        play(word)
    else:
        x = None
        print("Incorrect input")
        main()
    while input("Play Again? (Y/N) ").upper() == "Y":
        x = None
        main()                 

if __name__ == '__main__':
    main()                   

                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    