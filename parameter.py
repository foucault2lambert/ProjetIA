class Parameter:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.CHICKEN_COLOR = (0, 0, 255)  # Bleu
        self.FOX_COLOR = (255, 000, 0)  # Rouge
        self.SEED_COLOR = (0, 255, 0)  # Vert


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
