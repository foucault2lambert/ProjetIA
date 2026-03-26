class Parameter:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.CHICKEN_COLOR = (0, 0, 255)  # Bleu
        self.FOX_COLOR = (255, 000, 0)  # Rouge
        self.SEED_COLOR = (0, 255, 0)  # Vert
        self.NUM_CHICKENS = 20
        self.NUM_FOXES = 5


    def getWIDTH(self):
        return self.WIDTH

    def getHEIGHT(self):
        return self.HEIGHT

    def getCHICKEN_COLOR(self):
        return self.CHICKEN_COLOR

    def getFOX_COLOR(self):
        return self.FOX_COLOR

    def getSEED_COLOR(self):
        return self.SEED_COLOR

    def getNUM_CHICKENS(self):
        return self.NUM_CHICKENS
    def getNUM_FOXES(self):
        return self.NUM_FOXES