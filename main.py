import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((350, 600))
clock = pygame.time.Clock()

#player
player_image = pygame.image.load("assets/player_static.png").convert_alpha()
running = True

def draw():
    screen.fill('lightblue')
    screen.blit(player_image,(175,425))
# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw()



    clock.tick(60)
    pygame.display.update()
