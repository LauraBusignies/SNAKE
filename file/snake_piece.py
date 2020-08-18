# coding: utf-8

import pygame

# créer la classe des blocs serpent
class Snake_piece():

    def __init__(self, path):
        # Load le sprite du bloc du serpent
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (40, 40))
        # Créer le rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rotate = r
