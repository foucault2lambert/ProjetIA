import random
class Animal:
    def __init__(self, x, y, genes):
        self.x = x
        self.y = y
        self.energy = 100
        self.age = 0
        self.genes = genes  # Dictionnaire de traits mutables

    def move(self):
        # Logique de déplacement basée sur la vitesse (gène)
        self.x += random.uniform(-self.genes['speed'], self.genes['speed'])
        self.y += random.uniform(-self.genes['speed'], self.genes['speed'])
        self.energy -= self.genes['speed'] * 0.1  # Plus on va vite, plus on perd d'énergie