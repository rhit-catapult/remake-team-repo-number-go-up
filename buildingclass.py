import pygame
import sys

counselor = ""
cost1 = 0
building_aps = 0
building_amount = 0

counselors = ["faith", "jeffrey", "michael owens", "mary", "alex", "molly", "emre", "lorelai", "michael nelson",
                   "elley", "eathan"]
costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
building_aps = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 10000000000000]
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
a8 = 0
a9 = 0
a10 = 0
a11 = 0
a12 = 0
# building_amts = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
progression = 0
class Building:
    def __init__(self, screen):
        self.screen = screen
        #self.y = y

    def draw(self, screen):
        pygame.draw.rect(self.screen, (0, 255, 0), (screen.get_width()//2, 0))
    def update(self):
        pass
    def cost(self, inputbuilding, building_aps, building_amount, amount, amountpersecond):
        self.inputbuilding = inputbuilding
        cost1 = costs[inputbuilding]
        building_aps1 = building_aps[inputbuilding]

        amount = amount - cost1
        amountpersecond = amountpersecond + building_aps1
        building_amount = building_amount + 1
        cost1 = cost1 * 1.5
        return (amount, amountpersecond)
