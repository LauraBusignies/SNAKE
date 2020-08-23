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
        self.moove_snake = True 
        self.var_rotate_end = 0

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

    def turn_around(self, event):
        self.moove_snake = True 

        if self.snake.list_direction[len(self.snake.list_direction) -1] == "Y-" and event == "bas" :
            self.moove_snake = False 
        elif self.snake.list_direction[len(self.snake.list_direction) -1] == "Y+" and event == "haut" :
            self.moove_snake = False 
        elif self.snake.list_direction[len(self.snake.list_direction) -1] == "X-" and event == "droite" :
            self.moove_snake = False 
        elif self.snake.list_direction[len(self.snake.list_direction) -1] == "X+" and event == "gauche" :
            self.moove_snake = False 
        return self.moove_snake

    def rotate_end(self):
        self.var_rotate_end = 0
        if self.snake.list_direction[2] == "X+" :
            self.var_rotate_end = 0
        elif self.snake.list_direction[2] == "X-" :
            self.var_rotate_end = 180
        elif self.snake.list_direction[2] == "Y+" :
            self.var_rotate_end = -90
        else : 
            self.var_rotate_end = 90
        
    def middle_or_turn(self, new_rotate):
        if self.snake.list_direction[len(self.snake.list_direction) -1] == self.snake.list_direction[len(self.snake.list_direction) -2] :
            self.snake.list_body[len(self.snake.list_body) -1].image = pygame.image.load("assets/snake/middle.png")
            #self.snake.list_body[len(self.snake.list_body) -1].image = pygame.transform.scale(self.snake.list_body[len(self.snake.list_body) -1].image, (40, 40))
            self.snake.list_body[len(self.snake.list_body) -1].image = pygame.transform.rotate(self.snake.list_body[len(self.snake.list_body) -1].image, new_rotate)
        else : 
            self.snake.list_body[len(self.snake.list_body) -1].image = pygame.image.load("assets/snake/turn.png")
            #self.snake.list_body[len(self.snake.list_body) -1].image = pygame.transform.scale(self.snake.list_body[len(self.snake.list_body) -1].image, (40, 40))
            self.snake.list_body[len(self.snake.list_body) -1].image = pygame.transform.rotate(self.snake.list_body[len(self.snake.list_body) -1].image, new_rotate)

    def moove (self, event):
        self.turn_around(event)
        self.rotate_end()
        if self.moove_snake :

            new_Y = self.snake.list_body[len(self.snake.list_body) -1].rect.y
            new_X = self.snake.list_body[len(self.snake.list_body) -1].rect.x
            new_rotate = 0

            # changer la rotation de la pièce mileu
            if self.snake.list_direction[len(self.snake.list_direction) - 1] == self.snake.list_direction[len(self.snake.list_direction) - 2]:
                if self.snake.list_direction[len(self.snake.list_direction) - 1][0] == "X":
                    new_rotate = 0
                else:
                    if self.snake.list_direction[len(self.snake.list_direction) - 1][1] == "+":
                        new_rotate = 270
                    else:
                        new_rotate = 90

            # supprime le dernier bloc du serpent
            del self.snake.list_body[0]
            del self.snake.list_direction[0]
            # affiche la queue au bout de notre serpent
            self.snake.list_body[0].image = pygame.image.load("assets/snake/end.png")
            #self.snake.list_body[0].image = pygame.transform.scale(self.snake.list_body[0].image, (40, 40))
            self.snake.list_body[0].image = pygame.transform.rotate(self.snake.list_body[0].image, self.var_rotate_end)
                

            if event == "haut":
                self.snake.list_direction.append("Y-")
                new_Y -= 40
                self.middle_or_turn(new_rotate)
                self.snake.list_body.append(Snake_piece(new_X, new_Y, "assets/snake/start.png", 90))

            elif event == "bas":
                self.snake.list_direction.append("Y+")
                new_Y += 40
                self.middle_or_turn(new_rotate)
                self.snake.list_body.append(Snake_piece(new_X, new_Y, "assets/snake/start.png", -90))

            elif event == "gauche" :
                self.snake.list_direction.append("X-")
                new_X -= 40
                self.middle_or_turn(new_rotate)
                self.snake.list_body.append(Snake_piece(new_X, new_Y, "assets/snake/start.png", 180))

            else:
                self.snake.list_direction.append("X+")
                new_X += 40
                self.middle_or_turn(new_rotate)
                self.snake.list_body.append(Snake_piece(new_X, new_Y, "assets/snake/start.png", 0))


            
            # self.snake.list_body.append(Snake_piece(new_X, new_Y, "assets/snake/start.png", new_rotate))


    # list_2_d = ["Y-", "X+", "X+"]