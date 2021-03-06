import pygame
import math


from file.game import Game
pygame.init()



# generer la fenetre du jeu
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((1080, 720))

# importer et charger le background*
background = pygame.image.load('assets/background/background.png')
# background = pygame.transform.scale(background, (1080, 720))


# import charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/background/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = pygame.Surface.get_width(screen) / 2 - 200
play_button_rect.y = 300

game = Game()

running = True

# boucle tant que running est vrai
while running:

    # appliquer le background
    screen.blit(background, (0,0))

    # verifier si le jeu a commencou ou pas
    if game.is_playing:
        # declencher les instructiond de la partie
        game.update(screen)
    # si le jeu n'est pas lancer
    else:
        # ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)


    # update le screen
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # check que l'event est le fait de fermer la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu ce ferme")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier que la souris est appyer au bon endroit
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lander
                game.start()

        elif event.type == pygame.KEYDOWN :
            list_controller = {
                273 : "haut",
                275 : "droite",
                274 : "bas",
                276 : "gauche"
            }
            if event.key in list_controller:
                game.moove(list_controller[event.key])

            game.pressed[event.key] = True
            


        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False