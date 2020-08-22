# coding: utf-8

import pygame
from file.snake_piece import Snake_piece

# créer la classe des herbes
class Snake():

    def __init__(self):
        # ? création de la liste de piece du snake
        self.list_body = []
        self.list_direction = ["X+", "X+", "X+"]
        self.list_model = {
            "X+" : "→",
            "X-" : "←",
            "Y+" : "↓",
            "Y-" : "↑"
        }
        
        # ? speed du snake
        self.speed = 40
        
        # ? création des 3 premiers bloc du snake
        self.list_body.append(Snake_piece(200, 200, "assets/snake/end.png", 0))
        self.list_body.append(Snake_piece(240, 200, "assets/snake/middle.png", 0))
        self.list_body.append(Snake_piece(280, 200, "assets/snake/start.png", 0))
        