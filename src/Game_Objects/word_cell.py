import pygame
from assets.letter_dict import grid_dict
from assets.word_list import test_bro, real_bro

class Word_Cell:

    def __init__(self, columns, row_num, size, screen_width):
        self.columns = columns
        self.size = size

        # colours
        self.dark_colour = (60, 60, 60)
        self.light_colour = (100, 100, 100)
        self.green = "#5db54e"
        self.yellow = "#c9af16"

        self.gap = 5        # gap between each cell
        self.x = (1/2) * (screen_width - columns * (size + self.gap))   # centres the cell (x pos)
        self.y = 66 + row_num * (self.size + self.gap)                  # sets the y position of the word cell

        # handles logic and shit
        self.guess = ""
        self.target = real_bro

        self.entered = False      # checks if the word has been entered`
        self.result = ['_', '_', '_', '_', '_']   # keeps track of how well you guessed the word '_' is gray, '?' is yellow, '*' is green

    def backspace(self):
        self.guess = self.guess[:-1]

    def enter(self):
        if len(self.guess) < 5:
            print("word not long enough")
            return False
        
        self.word_check()
        self.entered = True
        return True

    def word_check(self):
        # keeps track of each letter and their count key = letter, value = amount of times that letter appears in the target
        bruddy = {}

        for char in self.guess:
            # use dictionary to keep track of crodies
            bruddy[char] = self.target.count(char)

        for i, char in enumerate(self.guess):
            if char == self.target[i]:
                self.result[i] = '*'
                bruddy[char] -= 1

        for i, char in enumerate(self.guess):
            if char in self.target and self.result[i] == '_' and bruddy[char] != 0:
                self.result[i] = '?'
                bruddy[char] -= 1
        print(self.result, bruddy)
        # self.result = ['_', '_', '_', '_', '_']
        # TODO implement the 6 guesses

    def type_word(self, key):
        if len(self.guess) < 5:
            self.guess += key

    def draw(self, surf):
        letter_offset = 10

        # draws the grid itself
        for i in range(self.columns):
            if not self.entered:
                pygame.draw.rect(surf, self.dark_colour, (i * (self.size + self.gap) + self.x, self.y, self.size, self.size), width=2)
                continue

            if self.result[i] == '_':
                pygame.draw.rect(surf, self.dark_colour, (i * (self.size + self.gap) + self.x, self.y, self.size, self.size))
            elif self.result[i] == '?':
                pygame.draw.rect(surf, self.yellow, (i * (self.size + self.gap) + self.x, self.y, self.size, self.size))
            elif self.result[i] == '*':
                pygame.draw.rect(surf, self.green, (i * (self.size + self.gap) + self.x, self.y, self.size, self.size))

        # draws the letters inside the grid
        for i, char in enumerate(self.guess):
            surf.blit(grid_dict[char], (i * (self.size + self.gap) + self.x + letter_offset, self.y))