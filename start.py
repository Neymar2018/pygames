# au préalable installer la bibliothèque pygame avec :
# pip install pygame
import pygame

pygame.init()
# déclarations de mes variables
fenetre = pygame.display.set_mode((640, 480))

background = pygame.image.load("./assets/img/background.jpg").convert()
goomba = pygame.image.load("./assets/img/goomba.png").convert_alpha()
mario = pygame.image.load("./assets/img/mario.png.webp").convert_alpha()
# importer le son
sound = pygame.mixer.Sound("./assets/audio/miaou.mp3")
# fonction de collision avec mario
def mario_collision(left, top):
    global mario,mario_rect
    print(f"position goomba left : {left}")
    print(f"position goomba top : {top}")
    if left < 50 and top < 70:
        print("Mario est mort")
       
        pygame.quit()
        exit()

goomba_rect = goomba.get_rect()
goomba_rect.topleft = (320, 240)
mario_rect = mario.get_rect()
mario_rect.topleft = (0, 0)

fenetre.blit(background, (0, 0))
# je crée une boucle
continuer = True
mario_speed = 5  # Vitesse de déplacement de Mario
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # touche Escape
                continuer = False

            # Déplacement de Mario avec les touches fléchées ou WASD
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if mario_rect.left < 500:
                    mario_rect = mario_rect.move(mario_speed, 0)
                    mario_collision(goomba_rect.left, goomba_rect.top)
                else:
                    sound.play()
            if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                if mario_rect.left > 0:
                    mario_rect = mario_rect.move(-mario_speed, 0)
                    mario_collision(goomba_rect.left, goomba_rect.top)
                else:
                    sound.play()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if mario_rect.top < 380:
                    mario_rect = mario_rect.move(0, mario_speed)
                    mario_collision(goomba_rect.left, goomba_rect.top)
                else:
                    sound.play()
            if event.key == pygame.K_UP or event.key == pygame.K_z:
                if mario_rect.top > 0:
                    mario_rect = mario_rect.move(0, -mario_speed)
                    mario_collision(goomba_rect.left, goomba_rect.top)
                else:
                    sound.play()

    fenetre.blit(background, (0, 0))
    fenetre.blit(goomba, goomba_rect)
    fenetre.blit(mario, mario_rect)
    pygame.display.update()

pygame.quit()
