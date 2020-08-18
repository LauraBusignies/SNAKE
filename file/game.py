# coding : utf-8

import pygame
import random
from file.snake import Snake

# créer une classe game
class Game:

    def __init__(self):
        # definir si le jeu a commencer ou pas
        self.is_playing = False
        self.pressed = {}

    def start(self):
        self.is_playing = True
        
    def end(self):
        self.is_playing = False

    def create_snake(self):
        pass

    def update(self, screen):
        pass

    def moove (self):
        pass

# list_2_d = ["Y-", "X+", "X+"]