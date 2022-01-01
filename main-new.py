import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Giera")

FPS = 60
VELOCITY = 5
BULLET_VELOCITY = 8
MAX_BULLETS = 3
BORDER = pygame.Rect((WIDTH-10)/2, 0, 10, HEIGHT)

# BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('sounds', 'name1.mp3'))
# BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('sounds', 'name2.mp3'))

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100) 

PATH = 'images'

FIRST_SPACESHIP = pygame.transform.rotate(pygame.image.load(os.path.join(PATH, 'spaceship.png')), 270)
SECOND_SPACESHIP = pygame.transform.rotate(pygame.image.load(os.path.join(PATH, 'spaceship.png')), 90)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, (0,0,0))
    WIN.blit(draw_text, ((WIDTH//2 - draw_text.get_width()//2), (HEIGHT//2 - draw_text.get_height()//2)))
    pygame.display.update()
    pygame.time.delay(5000)


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.fill((255,255,255))
    pygame.draw.rect(WIN, (0,0,0), BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, (0,0,0))
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, (0,0,0))

    WIN.blit(red_health_text, (10, 10))
    WIN.blit(yellow_health_text, (WIDTH - red_health_text.get_width() - 10, 10))

    WIN.blit(FIRST_SPACESHIP, (red.x, red.y))
    WIN.blit(SECOND_SPACESHIP, (yellow.x, yellow.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255,0,0), bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, (0,0,255), bullet)

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

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    # przesuwanie pocisków ale na razie bez sprites
    for bullet in yellow_bullets:
        bullet.x -= BULLET_VELOCITY
        if red.colliderect(bullet) and len(yellow_bullets) > 0:
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if bullet.right < 0 and len(red_bullets) > 0:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x += BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        if bullet.left > WIDTH:
            red_bullets.remove(bullet)



def main() :

    red = pygame.Rect(100, 300, FIRST_SPACESHIP.get_width(), FIRST_SPACESHIP.get_height())
    yellow = pygame.Rect(800, 300, SECOND_SPACESHIP.get_width(), FIRST_SPACESHIP.get_height())

    clock = pygame.time.Clock()
    running = True

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    winner_text = ""

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    red_bullet = pygame.Rect(red.right, red.centery, 10, 5)
                    red_bullets.append(red_bullet)
                    # BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                    yellow_bullet = pygame.Rect(yellow.left, yellow.centery, 10, 5)
                    yellow_bullets.append(yellow_bullet)
                    # BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                # BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                # BULLET_HIT_SOUND.play()

        if red_health <= 0:
            winner_text = "Yellow wins"

        if yellow_health <= 0:
            winner_text = "Red wins"

        if winner_text != "":
            draw_winner(winner_text)
            break


        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    main()


if __name__ == "__main__":
    main()
