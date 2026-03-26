import animal
from animal import Animal


class Chiken(Animal):
    def __init__(self, x, y, genes):
        super().__init__(x, y, genes)
        self.moveLikeChiken = genes['speed'] = 3  # Vitesse de déplacement spécifique aux poules

    def moveLikeChiken(self):
        self.x * self.moveLikeChiken