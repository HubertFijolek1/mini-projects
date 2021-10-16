import random
word_list=[]
with open("hangman_words.txt") as f:
    for l in f:
        word_list.append(l.strip())
f.close()


def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_covering = "_" * len(word)
    guessed = False
    number_of_tries = 6
    used_letters = []
    show_game(number_of_tries,word_covering, word)
    while not guessed and number_of_tries > 0:
        guess = input("guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in used_letters:
                print("you already tried", guess, "!")
            elif guess not in word:
                print(guess, "isn't in the word :(")
                number_of_tries -= 1
                print("Number of remaining attempts: %s" % number_of_tries)
                used_letters.append(guess)
            else:
                print("Nice one,", guess, "is in the word!")
                used_letters.append(guess)
                word_as_list = list(word_covering)
                for i in find_indexes(word, guess):
                    word_as_list[i]= guess
                word_covering = "".join(word_as_list)
                if word == word_covering:
                    guessed = True
        else:
            print("invalid input")
        print(display_hangman(number_of_tries))
        print(word_covering)
        print("\n")
    if guessed:
        print("Good Job, you guessed the word!")
    else:
        print("I'm sorry, but you ran out of tries. The word was " + word + ". Maybe next time!")
        
def show_game(number_of_tries,word_covering, word):
    print("Let's play hangman! :)")
    print(display_hangman(number_of_tries))
    print(word_covering)
    print()
def find_indexes(word, guess):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if guess == letter_in_word:
            indexes.append(index)
    
    return indexes

def display_hangman(number_of_tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[number_of_tries]


def main():
    word = get_word(word_list)
    play(word)
    while input("Again? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()
    