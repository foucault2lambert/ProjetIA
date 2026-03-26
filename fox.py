from animal import Animal


class Fox(Animal):
    def __init__(self, x, y, genes):
        super().__init__(x, y, genes)
        self.moveLikeFox = genes['speed'] = 5  # Vitesse de déplacement spécifique aux renard

    def moveLikeChiken(self):
        self.move()*self.moveLikeFox