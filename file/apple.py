# coding: utf-8

import pygame

# créer la classe des blocs serpent
class Apple():

    def __init__(self, x, y):
        # Load le sprite du bloc du serpent
        self.image = pygame.image.load("assets/snake/apple.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        # Créer le rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
