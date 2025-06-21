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
    amount = 10000000000000000
    amount_click = 1
    amount_second = 0
    famount = format(amount, ",")
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                distance1 = distance(mousepos, (screen.get_width()//4, screen.get_height()//2))
                if distance1 < screen.get_width()//8:
                    famount = famount + amount_click

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
        font2 = pygame.font.SysFont("calibri", 30)
        caption2 = font2.render("Amount: " + str(famount), True, (0, 0, 255))
        screen.blit(caption2, (screen.get_width()//40, screen.get_height()//6))
        pygame.display.update()


main()