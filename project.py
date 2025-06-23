import pygame
import sys
import time
import math
import random
from buildingclass import Building, building_aps, building_amount, cost1


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
    scroll_dis = 0
    progression = 0
    amount = 0
    amount_click = 1
    amountpersecond = 4
    secondlooptime = 0
    famount = format(amount, ",")
    famountpersecond = format(amountpersecond, ",")
    clock = pygame.time.Clock()
    prev_time = time.time()
    sw = screen.get_width()
    sh = screen.get_height()
    inputbuilding = 0
    test = Building(screen)
    rectlist = []
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                for i in range(len(rectlist)):
                    rect = rectlist[i]
                    if rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                        print(i)
                        inputbuilding = i
                        amount, amountpersecond = test.cost(inputbuilding, building_aps, building_amount, amount, amountpersecond)
                distance1 = distance(mousepos, (sw//4, sh//2))
                if distance1 < sw//8:
                    amount += amount_click
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    scroll_dis += sh//24
                if event.y < 0:
                    scroll_dis -= sh//24
        if scroll_dis > 0:
            scroll_dis = 0
        if scroll_dis < -1 * sh:
            scroll_dis = -1 * sh
        famount = format(amount, ",")
        famountpersecond = format(amountpersecond, ",")
        screen.fill((255, 255, 255))

        rectlist = [
            pygame.draw.rect(screen, (200, 200, 255), (sw//2, 0+scroll_dis, sw//2, sh//6)),
            pygame.draw.rect(screen, (150, 150, 255), (sw // 2, sh // 6+scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (100, 100, 255), (sw // 2, sh // 6*2+scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (50, 50, 255), (sw // 2, sh // 6*3+scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (0, 0, 255), (sw // 2, sh // 6*4+scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (0, 0, 220), (sw // 2, sh // 6 * 5+scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (0, 0, 185), (sw // 2, sh // 6 * 6 + scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (0, 0, 150), (sw // 2, sh // 6 * 7 + scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (0, 0, 115), (sw // 2, sh // 6 * 8 + scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (0, 0, 80), (sw // 2, sh // 6 * 9 + scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (0, 0, 45), (sw // 2, sh // 6 * 10 + scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (0, 0, 10), (sw // 2, sh // 6 * 11 + scroll_dis, sw // 2, sh // 6))
        ]



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
            amount = amount + amountpersecond
            pass # second game loop



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