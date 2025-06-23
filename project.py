import pygame
import sys
import time
import math
import random
from buildingclass import Building

#1:faith
#2:jeffrey
#3:michael owens
#4:mary
#5:alex
#6:molly
#7:emre
#8:lorelai
#9:anthony
#10:michael nelson
#11:elley
#12:eathan (best tower)
#akshad is the cookie

# TODO add buildings and all that code
# such as where they spawn, an image of the counselor, name, cost,
# amount of that building, and production rate p/s of the building


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
    counselors = ["faith", "jeffrey", "michael owens", "mary", "alex", "molly", "emre", "lorelai", "michael nelson",
                   "elley", "eathan"]
    costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    building_aps = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 10000000000000]
    amount = 0
    amount_click = 1
    amountpersecond = 0
    secondlooptime = 0
    famount = format(amount, ",")
    famountpersecond = format(amountpersecond, ",")
    clock = pygame.time.Clock()
    prev_time = time.time()
    sw = screen.get_width()
    sh = screen.get_height()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                distance1 = distance(mousepos, (sw//4, sh//2))
                if distance1 < sw//8:
                    amount += amount_click
        famount = format(amount, ",")
        famountpersecond = format(amountpersecond, ",")
        screen.fill((255, 255, 255))


        pygame.draw.rect(screen, (0, 255, 0), (sw//2, 0, sw//2, sh//6))
        pygame.draw.line(screen, (0, 0, 0), (sw//2,0), (sw//2,sh),     10)
        pygame.draw.line(screen, (0, 0, 0), (0, sh // 1.25), (sw // 2, sh//1.25), 10)
        pygame.draw.line(screen, (0, 0, 0), (0, 0), (sw, 0), 8)
        pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, sh),  8)
        pygame.draw.line(screen, (0, 0, 0), (0, sh), (sw, sh),8)
        pygame.draw.line(screen, (0, 0, 0), (sw, 0), (sw, sh),8) # BORDERS no touchy
        pygame.draw.circle(screen, (0, 0, 0), (sw//4, sh//2), (sw//8)) # placeholder cookie
        current_time = time.time()
        elapsed_time = current_time - prev_time
        prev_time = current_time
        fps = 1 / elapsed_time if elapsed_time > 0 else 0
        if secondlooptime % 60 == 0:
            print(counselors[0])
            pass # second game loop

        amount = amount + amountpersecond/60
        amount //= 1

        secondlooptime += 1



        font2 = pygame.font.SysFont("calibri", 30)
        caption2 = font2.render("Amount: " + str(famount), True, (0, 0, 255))
        screen.blit(caption2, (sw // 40, sh // 6))
        font3 = pygame.font.SysFont("calibri", 20)
        caption3 = font3.render("Aps: " + str(famountpersecond), True, (0, 0, 255))
        screen.blit(caption3, (sw // 40, sh // 4))



        pygame.display.set_caption("NGU's Project: "+ str(int(fps)))
        pygame.display.update()


main()