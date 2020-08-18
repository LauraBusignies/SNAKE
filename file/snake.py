# coding: utf-8

import pygame
from file.snake_piece import Snake_piece

# créer la classe des herbes
class Snake():

    def __init__(self, path, x, y):
        # ? création de la liste de piece du snake
        self.list_body = []
        # ? speed du snake
        self.speed = 40
        # ? création des 3 premiers bloc du snake
        self.list_body.append(self.create_part())
        self.list_body.append(self.create_part())
        self.list_body.append(self.create_part())
        
    def create_part(self):
        path = "assets/snqke/start.png"
        return Snake_piece(path)
