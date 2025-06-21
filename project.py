import pygame
import sys
import my_character
import random
import time


def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("NGU's Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((800, 600))

    # creates a Character from the my_character.py file


    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # draws the character every frame

        pygame.draw.line(screen, (255, 0, 0), (screen.get_width() / 2, 0), (screen.get_width() / 2, screen.get_height()),
                         10)
        pygame.draw.line(screen, (255, 0, 0), (0, 0), (screen.get_width(), 0),
                         8)
        pygame.draw.line(screen, (255, 0, 0), (0, 0), (0, screen.get_height()),
                         8)
        pygame.draw.line(screen, (255, 0, 0), (0, screen.get_height()), (screen.get_width(), screen.get_height()),
                         8)
        pygame.draw.line(screen, (255, 0, 0), (screen.get_width(), 0), (screen.get_width(), screen.get_height()),
                         8)
        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()

#test share