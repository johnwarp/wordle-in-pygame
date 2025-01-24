import pygame
from assets.letter_dict import letter_dict

class Button:
    
    def __init__(self, colour, x, y, width, height, border_radius, letter):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_radius = border_radius

        self.letter = letter

        self.rect = (x, y, width, height)
        self.pyrect = pygame.Rect(self.rect)

    def clicked(self, mouse_pos):
        if self.pyrect.collidepoint(mouse_pos):
            return True
        return False

    def draw(self, surf, mouse_pos):
        # draws the physical button
        pygame.draw.rect(surf, self.colour, (self.x, self.y, self.width, self.height), border_radius=self.border_radius)

        # blits the text on the keys
        try:
            surf.blit(letter_dict[self.letter], (self.x + 12, self.y + 7))
        except KeyError:
            pass

        # highlight
        if self.pyrect.collidepoint(mouse_pos):
            pygame.draw.rect(surf, "white", self.pyrect, width=2, border_radius=7)