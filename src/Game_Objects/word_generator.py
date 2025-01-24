import random, os

# os.chdir(os.path.dirname(os.path.abspath(__file__)))    # gets rid of errors (idk i found it on stackoverflow)

def choose_word():
    word_list = [] 

    with open('wordle/src/assets/words.txt') as file:     # creates the list of words
        word_list = [word.rstrip() for word in file.readlines()]

    index = random.randint(0, len(word_list) - 1)

    return word_list[index]