
counselors = ["faith", "jeffrey", "michael owens", "mary", "alex", "molly", "emre", "lorelai", "michael nelson",
                   "elley", "eathan"]
costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
building_aps = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 10000000000000]
building_amts = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
progression = 0
class Building:
    def __init__(self, screen, y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.y = y

    def draw(self):

    def update(self):
        pass
    def cost(self):
        pass

