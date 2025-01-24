import pygame, sys

from Game_Objects.button import Button
from Game_Objects.keyboard import Keyboard
from Game_Objects.word_cell import Word_Cell
import Game_Objects.word_generator as word_generator
from assets.letter_dict import letter_dict

# TODO implement peter griffin, he's gonna explain the etymology of each word you type

def main():

    # pygame setup
    pygame.init()
    WIDTH = 522
    HEIGHT = 720
    surf = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # regular bros
    running = True
    game_state = "gaming"

    current_row = 0
    update_row = False

    rows = 6

    # initialize objects
    kb = Keyboard()

    grid_list = [Word_Cell(columns=5, row_num=row, size=65, screen_width=WIDTH) for row in range(rows)]
    current_cell = grid_list[current_row]

    # fonts

    font = pygame.font.SysFont("Arial", 20)         # debugging purposes only
    text = font.render(current_cell.target, 1, "white")

    ending_text = font.render("ending the crodie is near", 1, "white")

    while running:
        mouse_pos = pygame.mouse.get_pos()

        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:            # takes inputs from the actual keyboard to the grid
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    current_cell.backspace()
                elif event.key == pygame.K_RETURN:
                    update_row = current_cell.enter()

                elif event.unicode.isalpha():
                    current_cell.type_word(event.unicode.upper())
            if event.type == pygame.MOUSEBUTTONDOWN:    # translates inputs from the onscreen keyboard to the grid
                key = kb.update(mouse_pos)
                if key == "backspace":     # makes sure that key isn't 'None'
                    current_cell.backspace()
                elif key == "enter":
                    update_row = current_cell.enter()
                elif key:
                    current_cell.type_word(key)

        if game_state == "gaming":
            
            # TODO remove the nesting (try using functions?)
            # updating cronems
            if update_row:
                current_row += 1

                guess = current_cell.guess
                kb.darken(guess)
                # changes game state after the final guess
                try:
                    current_cell = grid_list[current_row]
                except IndexError:
                    game_state = "end"
                update_row = False

            # fill the screen with a color to wipe away anything from last frame
            surf.fill("black")

            # RENDER YOUR GAME HERE
            # current_cell.draw(surf)
            for row in range(rows):
                grid_list[row].draw(surf)
            kb.draw(surf, mouse_pos)
            # surf.blit(text, (WIDTH / 2 - 10, 10))
        elif game_state == "end":
            pygame.draw.rect(surf, "blue", (100, 100, 200, 200))
            surf.blit(ending_text, (100, 100))
            surf.blit(text, (100, 120))

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    sys.exit()

main()