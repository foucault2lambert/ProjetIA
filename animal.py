import random
import math
import pygame
import pygame.gfxdraw

class Animal:
    def __init__(self, x, y, genes):
        self.pos = pygame.Vector2(x, y)
        self.angle = pygame.Vector2(1,0)
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
            self.genes = genes

        self.view_distance = genes.get("view_dist", 100.0)  # Portée en pixels
        self.view_angle = genes.get("view_angle", 100.0)  # Angle en degrés
        self.longevity =  genes.get("longevity", 500) # Âge maximum


    def move(self):
        # 1. On tourne un peu au hasard (on modifie le vecteur vel)
        rotation = random.uniform(-10, 10)  # Tourne de -10 à +10 degrés
        self.angle.rotate_ip(rotation)

        # 2. On avance dans la direction de self.vel
        # La position est mise à jour en ajoutant le vecteur vitesse
        self.pos += self.angle * self.genes['speed']

        # 3. Coût en énergie
        self.energy -= self.genes['speed'] * 0.1

    def older(self):
        self.age += 1
        return self.age

    def isDie(self):
        if self.age > self.genes['longevity'] or self.energy <= 0:
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

    def drawVision(self, screen, color=(100, 100, 100, 50)):
        #Récupération des paramètres (soit des gènes, soit des attributs)
        view_dist = self.view_distance
        view_angle = self.view_angle

        #Si l'animal est immobile ou sans direction, on ne dessine rien.
        if self.angle.length_squared() == 0:
            return

        # je récup l'angle de direction de l'animal en degrés (0° = vers la droite, 90° = vers le bas, etc.)
        base_angle = self.angle.as_polar()[1]

        # Un cône est un ensemble de vecteurs entre la Pos de l'animal et point_arc1, point_arc2, ..., point_arcN
        points = []

        # Premier point : le centre de l'animal
        points.append((int(self.pos.x), int(self.pos.y)))

        # Nombre de segments pour dessiner l'arc
        num_segments = 15

        # On calcule l'angle de départ et d'arrivée du cône
        start_angle = base_angle - (view_angle / 2)
        end_angle = base_angle + (view_angle / 2)

        # On génère les points le long de l'arc de cercle
        for i in range(num_segments + 1):
            angle_deg = start_angle + (i * (view_angle / num_segments))

            # Conversion en radians pour les fonctions math
            angle_rad = math.radians(angle_deg)

            # Calcul des coordonnées (x, y) du point sur l'arc
            # x = pos_x + distance * cos(angle)
            # y = pos_y + distance * sin(angle)
            px = self.pos.x + math.cos(angle_rad) * view_dist
            py = self.pos.y + math.sin(angle_rad) * view_dist

            points.append((int(px), int(py)))

        # --- 4. Dessin du polygone transparent ---
        # pygame.gfxdraw.filled_polygon() est la clé ici.
        # Attention : Contrairement à pygame.draw, gfxdraw ne gère pas
        # automatiquement la transparence si on dessine directement sur l'écran.
        # Il faut dessiner sur une surface intermédiaire (un "calque").

        # Création d'une surface temporaire de la taille de l'écran avec gestion alpha
        # (Cette étape peut être optimisée en créant une surface plus petite
        # juste autour de l'animal, mais pour commencer, c'est plus simple comme ça).
        overlay = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)

        # Dessiner le polygone rempli sur le calque
        pygame.gfxdraw.filled_polygon(overlay, points, color)

        # Dessiner le contour du polygone (optionnel, mais fait plus propre,
        # utiliser un alpha un peu plus fort)
        outline_color = (color[0], color[1], color[2], color[3] + 30)
        pygame.gfxdraw.aapolygon(overlay, points, outline_color)  # aa = anti-aliased

        # Appliquer le calque sur l'écran principal
        screen.blit(overlay, (0, 0))