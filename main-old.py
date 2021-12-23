import pygame
from pygame.constants import K_LEFT, KEYDOWN

screen_width = 800
screen_height = 600

pygame.init() # initialize pygame
screen = pygame.display.set_mode((screen_width, screen_height)) # creates a screeen with given dimensions
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("/home/patryk/Python_projects/pygame-basics/space-invaders.png")
pygame.display.set_icon(icon)

playerImage = pygame.image.load("/home/patryk/Python_projects/pygame-basics/spaceship.png")
playerX = 370
playerY = 480


def player(x, y):
    screen.blit(playerImage, (x, y)) # draw on screen


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                print("right")
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("released")
                playerX_change = 0
        
    playerX += playerX_change
    screen.fill((120,83,189))
    player(playerX, playerY)
    pygame.display.update()