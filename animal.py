import random
import math
import pygame

class Animal:
    def __init__(self, x, y, genes):
        self.x = x
        self.y = y
        self.pos = pygame.Vector2(self.x, self.y)
        self.angle = 90#pygame.Vector2(1,0)
        self.energy = 100
        self.age = 0
        if genes is None:
            self.genes = {
                "speed": 2.0,
                "view_dist": 100.0,
                "view_angle": 100.0,
                "longevity": 500  #age max
            }
        else:
            self.genes = genes  # Dictionnaire de traits mutables
        self.view_distance = genes.get('view_dist', 100)  # Portée en pixels
        self.view_angle = genes.get('view_angle', 10)  # Angle en degrés

    def drawVision(self, screen):
        # Dessiner le nez
        end_x = self.x + self.view_distance * math.cos(self.angle)
        end_y = self.y + self.view_distance * math.sin(self.angle)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (end_x, end_y), 5)
        # Dessiner les cônes de vision
        # Calculer les point exterieurs des lignes pour les côtés gauche et droit du cône de vision
        left_angle = self.angle - ((self.view_angle )/ 2)
        right_angle = self.angle + ((self.view_angle) / 2)
        left_end_x = self.x + self.view_distance * math.cos(left_angle)
        left_end_y = self.y + self.view_distance * math.sin(left_angle)
        right_end_x = self.x + self.view_distance * math.cos(right_angle)
        right_end_y = self.y + self.view_distance * math.sin(right_angle)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (right_end_x, right_end_y), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (left_end_x, right_end_y), 3)
        for i in range(1, 10):
            left_end_x = self.x + self.view_distance * math.cos(left_angle- (self.view_angle/10) * i)
            left_end_y = self.y + self.view_distance * math.sin(left_angle- (self.view_angle/10) * i)
            #pygame.draw.line(screen, (25, 25, 25), (self.x, self.y), (left_end_x, left_end_y), 1)
            #pygame.draw.line(screen, (25, 25, 25), (self.x, self.y), (right_end_x, right_end_y), 1)
            #left_end_x = left_end_x + self.view_distance * math.cos(left_angle) * i / 10
            #left_end_y = left_end_y + self.view_distance * math.sin(left_angle) * i / 10

    def move(self):
        # Logique de déplacement basée sur la vitesse (gène)
        self.angle = random.uniform(0, 180)
        self.x = self.x + self.genes['speed'] * math.cos(self.angle)
        self.y = self.y + self.genes['speed'] * math.sin(self.angle)
        self.energy -= self.genes['speed'] * 0.1  # Plus on va vite, plus on perd d'énergie

    def age(self):
        self.age += 1

    def isDie(self):
        if self.age > 100 or self.energy <= 0:
            return True
        else:
            return False

    def feeding(self):#a faire avec des test de collision avec les graines ou les poules pour les renards
        self.energy += 20

    def reproduce(self):
        if self.energy > 50:
            # on recupere les gènes des parents et on ajoute une mutation aléatoire
            new_genes = {key: value + random.uniform(-0.5, 0.5) for key, value in self.genes.items()}
            return Animal(self.x, self.y, new_genes)
        else:
            return None

    def can_see(self):
        # fonction pour tester si dans le champs de vision de l'animal il y a une autre entité via du ray casyting
        pass
