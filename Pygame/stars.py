# LISTS IN PYGAME

# - Lasers/bullets
# - stars
# - Particle effects
# - store a large number of enemies

import random

import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
stars = []
for _ in range(100):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    pos = (x, y)
    stars.append(pos)

player_x = WIDTH // 2
player_y = HEIGHT - 50

bullets = []
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            # create a bullet - add to bullet list
            bullet = [player_x, player_y - 25]
            bullets.append(bullet)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for pos in bullets:
        pos[1] -= 10


    # DRAWING
    screen.fill((0, 0, 50))  # always the first drawing command

    for x, y in stars:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 2, 2))
    
    # PLAYER
    pygame.draw.circle(screen, (255, 255, 100), (player_x, player_y), 25)

    # BULLETS
    for center in bullets:
        pygame.draw.circle(screen, (255, 0, 0), center, 10)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()