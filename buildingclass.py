import pygame
import sys


cost1 = 0
building_aps = 0


counselors = ["faith", "jeffrey", "michael owens", "mary", "alex", "molly", "emre", "lorelai", "anthony", "michael nelson",
                   "elley", "eathan"]
costs = [5, 75, 350, 1250, 3500, 15000, 80000, 390000, 1500000, 30000000, 1000000000, 100000000000]
building_aps = [1, 10, 35, 160, 400, 1000, 5000, 22500, 125000, 1000000, 50000000, 10000000000000]
building_amts = [0,0,0,0,0,0,0,0,0,0,0,0]

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

        if amount >= cost1:
            amount = amount - cost1
            amountpersecond = amountpersecond + building_aps1
            building_amts[inputbuilding] = building_amts[inputbuilding] + 1
            costs[inputbuilding] *= 12
            costs[inputbuilding] //= 10

        return (amount, amountpersecond)
