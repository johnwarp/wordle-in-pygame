import os, random
os.chdir(os.path.dirname(os.path.abspath(__file__)))   # gets rid of file not found error (from stackoverflow)

# initialize the file

with open('words.txt') as file:
    word_list = [x.rstrip() for x in file.readlines()]

# word list is the real gamer

with open('bruh.txt') as file:
    test_bruh = [x.rstrip() for x in file.readlines()]

test_bro = test_bruh[random.randint(0, len(test_bruh)-1)].upper()
real_bro = word_list[random.randint(0, len(word_list)-1)].upper()