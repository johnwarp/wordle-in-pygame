import pygame
# TODO rename this file to font_dict or somethign more accurate than this shit

pygame.font.init()      # initializes font, this is required or the program shits itself

keyboard_font = pygame.font.SysFont("Comic Sans", 30)
grid_font = pygame.font.SysFont("Papyrus", 45)
crodie_bob = "QWERTYUIOPASDFGHJKLZXCVBNM"
letter_colour = "white"

letter_dict = {}    # fonts for the letters on the keyboard

for bro in crodie_bob:
    letter_dict[bro] = keyboard_font.render(bro, 1, letter_colour)

grid_dict = {}      # fonts for the letters in the grid

for bro in crodie_bob:
    grid_dict[bro] = grid_font.render(bro, 1, letter_colour)
