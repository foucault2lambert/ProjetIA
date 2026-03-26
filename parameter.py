class Parameter:
    def __init__(self,WIDTH, HEIGHT, CHICKEN_COLOR, FOX_COLOR, SEED_COLOR, NUM_CHICKENS, NUM_FOXES, NUM_SEED, CHICKEN_SIZE, FOX_SIZE, SEED_SIZE):
        #taille de la fenetre
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        #couleurs
        self.CHICKEN_COLOR = CHICKEN_COLOR
        self.FOX_COLOR = FOX_COLOR
        self.SEED_COLOR = SEED_COLOR

        #nombre de poules, renard et graines
        self.NUM_CHICKENS = NUM_CHICKENS
        self.NUM_FOXES = NUM_FOXES
        self.NUM_SEED = NUM_SEED

        #taille des poules, renard et graines
        self.CHICKEN_SIZE = CHICKEN_SIZE
        self.FOX_SIZE = FOX_SIZE
        self.SEED_SIZE = SEED_SIZE

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

    def getNUM_SEED(self):
        return self.NUM_SEED