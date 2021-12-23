import pygame
import os

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Giera")

FPS = 60
VELOCITY = 5
BULLET_VELOCITY = 8
BORDER = pygame.Rect((WIDTH-10)/2, 0, 10, HEIGHT)

PATH = 'images'

FIRST_SPACESHIP = pygame.transform.rotate(pygame.image.load(os.path.join(PATH, 'spaceship.png')), 270)
SECOND_SPACESHIP = pygame.transform.rotate(pygame.image.load(os.path.join(PATH, 'spaceship.png')), 90)

def draw_window(red, yellow):
    WIN.fill((255,255,255))
    pygame.draw.rect(WIN, (0,0,0), BORDER)
    WIN.blit(FIRST_SPACESHIP, (red.x, red.y))
    WIN.blit(SECOND_SPACESHIP, (yellow.x, yellow.y))

    pygame.display.update()

def yellow_handle_movement(keys, yellow):
    
    if keys[pygame.K_a] and yellow.left - VELOCITY > (WIDTH - 10)/2: # LEFT
        yellow.x -= VELOCITY
    if keys[pygame.K_d] and yellow.right + VELOCITY < WIDTH: # LEFT
        yellow.x += VELOCITY
    if keys[pygame.K_w] and yellow.top - VELOCITY > 0: # LEFT
        yellow.y -= VELOCITY
    if keys[pygame.K_s] and yellow.bottom - VELOCITY < HEIGHT: # LEFT
        yellow.y += VELOCITY

def red_handle_movement(keys, red):
    
    if keys[pygame.K_LEFT] and red.left - VELOCITY > 0: # LEFT
        red.x -= VELOCITY
    if keys[pygame.K_RIGHT] and red.right + VELOCITY < (WIDTH - 10)/2: # LEFT
        red.x += VELOCITY
    if keys[pygame.K_UP] and red.top - VELOCITY > 0: # LEFT
        red.y -= VELOCITY
    if keys[pygame.K_DOWN] and red.bottom + VELOCITY < HEIGHT: # LEFT
        red.y += VELOCITY


def main() :

    red = pygame.Rect(100, 300, FIRST_SPACESHIP.get_width(), FIRST_SPACESHIP.get_height())
    yellow = pygame.Rect(800, 300, SECOND_SPACESHIP.get_width(), FIRST_SPACESHIP.get_height())

    clock = pygame.time.Clock()
    running = True

    red_bullets = []
    yellow_bullets = []

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    red_bullet = pygame.Rect(red.centery, red.right, 10, 5)
                    red_bullets.append(red_bullet)
                if event.key == pygame.K_RCTRL:
                    yellow_bullet = pygame.Rect(yellow.centery, yellow.left, 10, 5)
                    yellow_bullets.append(yellow_bullet)


        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
