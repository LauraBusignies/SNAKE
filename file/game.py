# coding : utf-8

import pygame
import random
from file.snake import Snake
from file.snake_piece import Snake_piece

# créer une classe game
class Game:

    def __init__(self):
        # definir si le jeu a commencer ou pas
        self.is_playing = False
        self.pressed = {}
        # definir le background
        self.background = pygame.image.load('assets/background/background.png')
        self.background = pygame.transform.scale(self.background, (1080, 720))

    def start(self):
        self.is_playing = True
        self.snake = Snake()
        
    def end(self):
        self.is_playing = False

    def create_snake_move(self):
        pass

    def update(self, screen):
        screen.blit(self.background, (0,0))
        for bloc in self.snake.list_body:
            screen.blit(bloc.image, bloc.rect)

    def moove (self, event):
        new_Y = self.snake.list_body[len(self.snake.list_body) -1].rect.y
        new_X = self.snake.list_body[len(self.snake.list_body) -1].rect.x
        new_rotate = 0
        
        if event == "haut":
            self.snake.list_direction.append("Y-")
            new_Y -= 40
        elif event == "bas":
            self.snake.list_direction.append("Y+")
            new_Y += 40
        elif event == "gauche" :
            self.snake.list_direction.append("X-")
            new_X -= 40
        else:
            self.snake.list_direction.append("X+")
            new_X += 40
            
        if self.snake.list_direction[len(self.snake.list_direction) - 1] == self.snake.list_direction[len(self.snake.list_direction) - 2]:
            if self.snake.list_direction[len(self.snake.list_direction) - 1][0] == "X":
                new_rotate = 0
            else:
                new_rotate = 90
        
        # supprime le dernier bloc du serpent
        del self.snake.list_body[0]
        # affiche la queue au bout de notre serpent
        self.snake.list_body[0].image = pygame.image.load("assets/snake/end.png")
        self.snake.list_body[0].image = pygame.transform.scale(self.snake.list_body[0].image, (40, 40))
        
        self.snake.list_body[len(self.snake.list_body) -1].image = pygame.image.load("assets/snake/middle.png")
        self.snake.list_body[len(self.snake.list_body) -1].image = pygame.transform.scale(self.snake.list_body[len(self.snake.list_body) -1].image, (40, 40))
        
        self.snake.list_body.append(Snake_piece(new_X, new_Y, "assets/snake/start.png", new_rotate))


# list_2_d = ["Y-", "X+", "X+"]