import pygame
from Game_Objects.button import Button

# TODO currently all the keys are being checked if they're being clicked every frame, maybe optimize that by doing something different?

class Keyboard:

    def __init__(self):
        # variabels to help initialize the rows
        pos_x = 2
        pos_y = 518
        width = 50
        height = 65
        border_radius = 7
        light_key_colour = 150
        dark_key_colour = 60

        top_str = "QWERTYUIOP"
        home_str = "ASDFGHJKL"
        bottom_str = "ZXCVBNM"

        top_row = []
        home_row = []
        bottom_row = []

        # initializes the rows
        for count, char in enumerate(top_str):
            top_row.append(Button((light_key_colour, light_key_colour, light_key_colour), pos_x + count * (width + 2), pos_y, width, height, border_radius, char))

        for count, char in enumerate(home_str):
            home_row.append(Button((light_key_colour, light_key_colour, light_key_colour), pos_x + width/2 + count * (width + 2), pos_y + height + 2, width, height, border_radius, char))
        
        for count, char in enumerate(bottom_str):
            bottom_row.append(Button((light_key_colour, light_key_colour, light_key_colour), 2 + pos_x + (3/2)*width + count * (width + 2), pos_y + 2 * height + 4, width, height, border_radius, char))
        
        # TODO this is the cause for the try except statement in button.py
        bottom_row.insert(0, Button((light_key_colour, light_key_colour, light_key_colour), pos_x, pos_y + 2 * height + 4, (3/2)*width, height, border_radius, "enter"))
        bottom_row.append(Button((light_key_colour, light_key_colour, light_key_colour), 2 + pos_x + (17/2)*width + 14, pos_y + 2 * height + 4, (3/2)*width + 2, height, border_radius, "backspace"))

        self.keyboard = top_row + home_row + bottom_row     # list of button objects

    def update(self, mouse_pos):
        # light = (150, 150, 150)
        # dark = (60, 60, 60)

        # returns the key corresponding to the button that is clicked
        for button in self.keyboard:
            if button.clicked(mouse_pos):
                return button.letter

    def darken(self, used_cro):
        for button in self.keyboard:
            if button.letter in used_cro:
                button.colour = (60, 60, 60)

    def draw(self, surf, mouse_pos):
        # draws each button in the keyboard
        for button in self.keyboard:
            button.draw(surf, mouse_pos)