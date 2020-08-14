# coding: utf-8

import pygame
from file.snake_piece import Snake_piece

# créer la classe des herbes
class Snake():

    def __init__(self, path, x, y):
        # ? création de la liste de piece du snake
        self.list_body = []
        # ? speed du snake
        self.speed = 75
        # ? création des 3 premiers bloc du snake
        self.list_body.append(self.create_part("start", 500, 500))
        self.list_body.append(self.create_part("middle", 425, 500))
        self.list_body.append(self.create_part("end", 350, 500))
        
    def create_part(self, block, x, y):
        if block == "start":
            path = "assets/snqke/start.png"
        elif block == "end":
            path = "assets/snqke/end.png"
        elif block == "middle":
            path = "assets/snqke/middle.png"
        elif block == "turn":
            path = "assets/snqke/turn.png"
        
        return Snake_piece(path, x, y)