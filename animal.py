import random
import math
class Animal:
    def __init__(self, x, y, genes):
        self.x = x
        self.y = y
        self.angle = 30#random.uniform(0,30)
        self.energy = 100
        self.age = 0
        self.genes = genes  # Dictionnaire de traits mutables

    def move(self):
        # Logique de déplacement basée sur la vitesse (gène)
        self.angle = random.uniform(0, 30)
        self.x = self.x + self.genes['speed'] * math.cos(self.angle)
        self.y = self.y + self.genes['speed'] * math.sin(self.angle)
        self.energy -= self.genes['speed'] * 0.1  # Plus on va vite, plus on perd d'énergie

    def age(self):
        self.age += 1

    def die(self):
        if self.age > 100 or self.energy <= 0:
            return True
        else:
            return False
    def feeding(self):
        self.energy += 20

    def reproduce(self):
        if self.energy > 50:
            # on recuypere les gènes des parents et on ajoute une mutation aléatoire
            new_genes = {key: value + random.uniform(-0.5, 0.5) for key, value in self.genes.items()}
            return Animal(self.x, self.y, new_genes)
        else:
            return None