import pygame
from assets.letter_dict import grid_dict
from assets.word_list import test_bro, real_bro

class Grid:

    def __init__(self, columns, rows, size, screen_width):
        self.columns = columns
        self.rows = rows
        self.size = size

        self.dark_colour = (60, 60, 60)
        self.light_colour = (100, 100, 100)

        self.gap = 5        # gap between each cell
        self.x = (1/2) * (screen_width - columns * (size + self.gap))   # horizontally centers the grid
        self.y = 516 - rows * (size + 2*self.gap)                       # makes it above the keyboard or something

        # handles logic and shit
        self.guess = ""
        self.target = real_bro

        self.result = ['_', '_', '_', '_', '_']   # keeps track of how well you guessed the word '_' is gray, '?' is yellow, '*' is green

        self.row = 1
        self.column = 0

    def backspace(self):
        self.guess = self.guess[:-1]

    def enter(self):
        if len(self.guess) < 5:
            print("word not long enough")
        else:
            self.word_check()

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
            if self.result[i] == '_' and char in self.target and bruddy[char] != 0:
                self.result[i] = '?'
                bruddy[char] -= 1
        print(self.result)
        self.result = ['_', '_', '_', '_', '_']
        # TODO implement the 6 guesses

    def type_word(self, key):
        if len(self.guess) < 5:
            self.guess += key

    def draw(self, surf):
        letter_offset = 10

        # draws the grid itself
        for i in range(self.rows):
            for j in range(self.columns):
                pygame.draw.rect(surf, self.dark_colour, (j * (self.size + self.gap) + self.x, i * (self.size + self.gap) + self.y, self.size, self.size), width=2)

        # draws the letters inside the grid
        for i, char in enumerate(self.guess):
            surf.blit(grid_dict[char], (i * (self.size + self.gap) + self.x + letter_offset, self.row * (self.size + self.gap) + self.y))