import pygame
import sys
import random
import time
import math
def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]
    return math.sqrt((point1_x - point2_x)**2 + (point1_y - point2_y)**2)

def main():
    pygame.init()
    pygame.display.set_caption("NGU's Project")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                print(mousepos)
                distance1 = distance(mousepos, (screen.get_width()//4, screen.get_height()//2))
                print(distance1)
                if distance1 < screen.get_width()//8:
                    print(distance1)

            # TODO: Add you events code

        screen.fill((255, 255, 255))

        pygame.draw.line(screen, (255, 0, 0), (screen.get_width() // 2, 0), (screen.get_width() // 2, screen.get_height()),
                         10)
        pygame.draw.line(screen, (255, 0, 0), (0, 0), (screen.get_width(), 0),
                         8)
        pygame.draw.line(screen, (255, 0, 0), (0, 0), (0, screen.get_height()),
                         8)
        pygame.draw.line(screen, (255, 0, 0), (0, screen.get_height()), (screen.get_width(), screen.get_height()),
                         8)
        pygame.draw.line(screen, (255, 0, 0), (screen.get_width(), 0), (screen.get_width(), screen.get_height()),
                         8)
        pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()/4, screen.get_height()/2), screen.get_width()/8)
        # TODO: Add your project code

        pygame.display.update()


main()