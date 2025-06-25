import pygame
import sys
import time
import math
import random
from buildingclass import Building, counselors, building_aps, building_amts, cost1, costs

def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]
    return math.sqrt((point1_x - point2_x)**2 + (point1_y - point2_y)**2)

def shop(x):
    shop_cost = []
    shop_name = []
    shop_desc = []
    shop_buff = []


def main():
    pygame.init()
    pygame.display.set_caption("NGU's Project")
    screen = pygame.display.set_mode((800, 600))
    scroll_dis = 0
    image1 = pygame.image.load("./samples/faith.JPEG")
    image2 = pygame.image.load("./samples/jeffrey.JPEG")
    image3 = pygame.image.load("./samples/owens.JPEG")
    image4 = pygame.image.load("./samples/mary.JPEG")
    image5 = pygame.image.load("./samples/alex.JPEG")
    image6 = pygame.image.load("./samples/molly.JPEG")
    image7 = pygame.image.load("./samples/emre.JPEG")
    image8 = pygame.image.load("./samples/lorelai.JPEG")
    image9 = pygame.image.load("./samples/anthony.JPEG")
    image10 = pygame.image.load("./samples/nelson.JPEG")
    image11 = pygame.image.load("./samples/elley.JPEG")
    image12 = pygame.image.load("./samples/eathan.JPEG")  # the boat (best of all time!!!!!!!!!!!!!!!0
    image13 = pygame.image.load("./samples/akshadcropped.png")
    GREY = (130, 130, 130)
    amount = 100000000000000
    amount_click = 1
    amountpersecond = 0
    secondlooptime = 0
    famount = format(amount, ",")
    famountpersecond = format(amountpersecond, ",")
    clock = pygame.time.Clock()
    prev_time = time.time()
    sw = screen.get_width()
    sh = screen.get_height()
    image1 = pygame.transform.scale(image1, (sh//6,sh//6))
    image2 = pygame.transform.scale(image2, (sh//6,sh//6))
    image3 = pygame.transform.scale(image3, (sh//6,sh//6))
    image4 = pygame.transform.scale(image4, (sh//6,sh//6))
    image5 = pygame.transform.scale(image5, (sh//6,sh//6))
    image6 = pygame.transform.scale(image6, (sh//6,sh//6))
    image7 = pygame.transform.scale(image7, (sh//6,sh//6))
    image8 = pygame.transform.scale(image8, (sh//6,sh//6))
    image9 = pygame.transform.scale(image9, (sh//6,sh//6))
    image10 = pygame.transform.scale(image10, (sh//6,sh//6))
    image11 = pygame.transform.scale(image11, (sh//6,sh//6))
    image12 = pygame.transform.scale(image12, (sh//6,sh//6))
    image13 = pygame.transform.scale(image13, (sh//3,sh//2.5))
    inputbuilding = 0
    test = Building(screen)
    rectlist = []
    linelist = []
    shop2list = [] #upgrades
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
                        inputbuilding = i
                        amount, amountpersecond = test.cost(inputbuilding, building_aps, building_amts, amount, amountpersecond)

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
            pygame.draw.rect(screen, (GREY), (sw//2, 0+scroll_dis, sw//2, sh//6)),
            pygame.draw.rect(screen, (GREY), (sw // 2, sh // 6+scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (GREY), (sw // 2, sh // 6*2+scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (GREY), (sw // 2, sh // 6*3+scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (GREY), (sw // 2, sh // 6*4+scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (GREY), (sw // 2, sh // 6 * 5+scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (GREY), (sw // 2, sh // 6 * 6 + scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (GREY), (sw // 2, sh // 6 * 7 + scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (GREY), (sw // 2, sh // 6 * 8 + scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (GREY), (sw // 2, sh // 6 * 9 + scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (GREY), (sw // 2, sh // 6 * 10 + scroll_dis, sw // 2, sh // 6)),
            pygame.draw.rect(screen, (GREY), (sw // 2, sh // 6 * 11 + scroll_dis, sw // 2, sh // 6))
        ]
        screen.blit(image1, (sw//2+sw//60, sh//6*0+scroll_dis))
        screen.blit(image2, (sw // 2 + sw // 60, sh // 6 + scroll_dis))
        screen.blit(image3, (sw // 2 + sw // 60, sh // 6 * 2 + scroll_dis))
        screen.blit(image4, (sw // 2 + sw // 60, sh // 6 * 3 + scroll_dis))
        screen.blit(image5, (sw // 2 + sw // 60, sh // 6 * 4 + scroll_dis))
        screen.blit(image6, (sw // 2 + sw // 60, sh // 6 * 5 + scroll_dis))
        screen.blit(image7, (sw // 2 + sw // 60, sh // 6 * 6 + scroll_dis))
        screen.blit(image8, (sw // 2 + sw // 60, sh // 6 * 7 + scroll_dis))
        screen.blit(image9, (sw // 2 + sw // 60, sh // 6 * 8 + scroll_dis))
        screen.blit(image10, (sw // 2 + sw // 60, sh // 6 * 9 + scroll_dis))
        screen.blit(image11, (sw // 2 + sw // 60, sh // 6 * 10 + scroll_dis))
        screen.blit(image12, (sw // 2 + sw // 60, sh // 6 * 11 + scroll_dis))

        linelist = [
            pygame.draw.line(screen, (50, 50, 50), (sw // 2, sh // 6 + scroll_dis), (sw, sh // 6 + scroll_dis), 8),
            pygame.draw.line(screen, (50, 50, 50), (sw // 2, sh // 6 * 2 + scroll_dis), (sw, sh // 6 * 2 + scroll_dis),
                             8),
            pygame.draw.line(screen, (50, 50, 50), (sw // 2, sh // 6 * 3 + scroll_dis), (sw, sh // 6 * 3 + scroll_dis),
                             8),
            pygame.draw.line(screen, (50, 50, 50), (sw // 2, sh // 6 * 4 + scroll_dis), (sw, sh // 6 * 4 + scroll_dis),
                             8),
            pygame.draw.line(screen, (50, 50, 50), (sw // 2, sh // 6 * 5 + scroll_dis), (sw, sh // 6 * 5 + scroll_dis),
                             8),
            pygame.draw.line(screen, (50, 50, 50), (sw // 2, sh // 6 * 6 + scroll_dis), (sw, sh // 6 * 6 + scroll_dis),
                             8),
            pygame.draw.line(screen, (50, 50, 50), (sw // 2, sh // 6 * 7 + scroll_dis), (sw, sh // 6 * 7 + scroll_dis),
                             8),
            pygame.draw.line(screen, (50, 50, 50), (sw // 2, sh // 6 * 8 + scroll_dis), (sw, sh // 6 * 8 + scroll_dis),
                             8),
            pygame.draw.line(screen, (50, 50, 50), (sw // 2, sh // 6 * 9 + scroll_dis), (sw, sh // 6 * 9 + scroll_dis),
                             8),
            pygame.draw.line(screen, (50, 50, 50), (sw // 2, sh // 6 * 10 + scroll_dis),
                             (sw, sh // 6 * 10 + scroll_dis), 8),
            pygame.draw.line(screen, (50, 50, 50), (sw // 2, sh // 6 * 11 + scroll_dis),
                             (sw, sh // 6 * 11 + scroll_dis), 8),
            pygame.draw.line(screen, (50, 50, 50), (sw // 2, sh // 6 * 12 + scroll_dis),
                             (sw, sh // 6 * 12 + scroll_dis), 8)

        ]
        pygame.draw.line(screen, (0, 0, 0), (sw//2,0), (sw//2,sh),     10)
        # pygame.draw.line(screen, (0, 0, 0), (0, sh // 1.25), (sw // 2, sh//1.25), 10)
        pygame.draw.line(screen, (0, 0, 0), (0, 0), (sw, 0), 8)
        pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, sh),  8)
        pygame.draw.line(screen, (0, 0, 0), (0, sh), (sw, sh),8)
        pygame.draw.line(screen, (0, 0, 0), (sw, 0), (sw, sh),8) # BORDERS no touchy
        # pygame.draw.circle(screen, (0, 0, 0), (sw//4, sh//2), (sw//8)) # placeholder cookie
        current_time = time.time()
        elapsed_time = current_time - prev_time
        prev_time = current_time
        fps = 1 / elapsed_time if elapsed_time > 0 else 0
        if secondlooptime % 60 == 0:

            if amountpersecond < 60:
                amount += amountpersecond
            pass # second game loop
        if amountpersecond >= 60:
            amount = amount + amountpersecond//60
        amount //= 1
        secondlooptime += 1
        font2 = pygame.font.SysFont("calibri", sh // 22)
        amont = pygame.font.SysFont("calibri", sh // 15)
        caption2 = font2.render(  str(famount), True, (0, 0, 0))
        caption1 = font2.render(str(counselors[0]), True, (0, 0, 255))
        #🍝🍝🍝🍝
        for i in range(12):
            caption1 = font2.render(str(counselors[i]), True, (255, 255, 255))
            screen.blit(caption1, (sw//2 + sw//6, sh // 60 + (i * sh//6) + scroll_dis))
            fcost = format(costs[i], ",")
            fcamppersec = format(building_aps[i], ",")
            famts = format(building_amts[i], ",")
            captioncost = font2.render("Cost: "+ str(fcost), True, (255, 255, 255))
            screen.blit(captioncost, (sw//2 + sw//6, sh // 60 + (i * sh//6) + sh//20 + scroll_dis))
            captionoftheaps = font2.render("CPS: " + str(fcamppersec), True, (255, 255, 255))
            screen.blit(captionoftheaps, (sw // 2 + sw // 6, sh // 60 + (i * sh // 6) + sh // 20*2 + scroll_dis))
            captionamt = font2.render(str(famts), True, (255, 255, 255))
            screen.blit(captionamt, (sw // 2 + sw // 5*2, sh // 60 + (i * sh // 6) + scroll_dis))

        screen.blit(caption2, (sw // 4.5  - len(famount)*5, sh // 7))

        font3 = pygame.font.SysFont("calibri", sh//32)
        caption3 = font3.render("CPS: " + str(famountpersecond), True, (0, 0, 0))
        screen.blit(caption3, (sw // 40, sh // 5+sh//40))


        pygame.draw.line(screen, (0, 0, 0), (sw // 2, 0), (sw // 2, sh), 10)
        pygame.draw.line(screen, (0, 0, 0), (0, sh // 1.25), (sw // 2, sh // 1.25), 10)
        pygame.draw.line(screen, (0, 0, 0), (0, 0), (sw, 0), 8)
        pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, sh), 8)
        pygame.draw.line(screen, (0, 0, 0), (0, sh), (sw, sh), 8)
        pygame.draw.line(screen, (0, 0, 0), (sw, 0), (sw, sh), 8)  # BORDERS no touchy
        screen.blit(image13, (sw // 8.5, sh // 3.5))
        pygame.display.set_caption("NGU's Project: "+ str(int(fps)))
        pygame.display.update()


main()
