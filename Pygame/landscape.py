# pygame template

import pygame
import random

pygame.init()

WIDTH = 720
HEIGHT = 450
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
game_tick = 0 # max 960
sun_x = -30
sun_y = 100
sun_color = (255, 215, 0)
sun_radius = 30
sky_color = [73.5, 113, 152] # noon (135, 206, 235) midnight (12, 20, 69)
window_color = (221, 221, 255) # lights off (221, 221, 255) lights on (255, 213, 61)
stars_coords = []
star_alpha = 0
weather = 1 # 1 = sunny, 2 = cloudy, 3 = rainy, 4 = thunderstorm
# 1 -> no new clouds
# 2 -> lots of new clouds
# 3 -> bit of new clouds and rain
# 4 -> a bunch of new clouds and rain and thunder
cloud_coords = []
speed_multiplier = 1
prev_weather = 0
rain_alpha = 0
thunder_this_frame = False

# ---------------------------

def random_star_coords():
    for _ in range(20):
        stars_coords.append((random.randint(0, WIDTH), random.randint(0, 200)))

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: # right arrow key to speed things up if you want to see weather changes faster
            speed_multiplier = 4 # highly recommend using this to see the weather changes faster
        else:
            speed_multiplier = 1

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # changes upon time of day
    if game_tick % 960 == 0:
        print("Morning")
        print(sky_color)
        prev_weather = weather
        weather = random.randint(1, 4)
        # weather = 4
        if weather != 1:
            num_clouds = 0
            if weather == 2:
                num_clouds = 5
            elif weather == 3:
                num_clouds = 10
            elif weather == 4:
                num_clouds = 20 # i love clouds
            for i in range(num_clouds):
                cloud_coords.append([random.randint(0, WIDTH) - WIDTH - 100, random.randint(30, 70)])
        stars_coords = []
        sun_color = (255, 215, 0)
        window_color = (221, 221, 255)
        print("Weather:", weather)
    elif game_tick % 960 == 240:
        print("Noon")
        print(sky_color)
    elif game_tick % 960 == 480:
        print("Night")
        print(sky_color)
        random_star_coords()
        sun_color = (246, 241, 213)
        window_color = (255, 213, 61)
    elif game_tick % 960 == 720:
        print("Midnight")
        print(sky_color)

    # changes during time of day
    sun_x += 1.6270833333
    if game_tick % 960 < 240: # morning-noon
        sun_y -= 0.3
        sky_color[0] += 0.25625 / weather
        sky_color[1] += 0.3875 / weather
        sky_color[2] += 0.3458333333 / weather
    elif game_tick % 960 < 480: # noon-night
        sun_y += 0.3
        sky_color[0] -= 0.25625 / weather
        sky_color[1] -= 0.3875 / weather
        sky_color[2] -= 0.3458333333 / weather
    elif game_tick % 960 < 720: # night-midnight
        sun_y -= 0.3
        sky_color[0] -= 0.25625
        sky_color[1] -= 0.3875
        sky_color[2] -= 0.3458333333
        star_alpha += 1.0625
    else: # midnight-morning
        sun_y += 0.3
        sky_color[0] += 0.25625
        sky_color[1] += 0.3875
        sky_color[2] += 0.3458333333
        star_alpha -= 1.0625


    if sun_x >= WIDTH + sun_radius:
        sun_x = -sun_radius

    thunder_this_frame = weather == 4 and random.randint(0, 20) == 0

    game_tick += 1

    # DRAWING

    if thunder_this_frame:
        screen.fill((135, 206, 235)) # epilepsy warning
    else:
        screen.fill(tuple(sky_color))  # always the first drawing command
    pygame.draw.rect(screen, (63, 155, 11), (0, 350, WIDTH, 100)) # ground

    # stars
    stars_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for star in stars_coords:
        pygame.draw.circle(stars_surface, (255, 242, 32, star_alpha), star, 2)
    screen.blit(stars_surface, (0, 0))
    

    # house
    pygame.draw.rect(screen, (170, 74, 68), (285, 200, 150, 150)) # house body
    pygame.draw.polygon(screen, (92, 64, 51), [(285, 200), (435, 200), (360, 130)]) # roof
    pygame.draw.rect(screen, window_color, (305, 260, 40, 40)) # window
    pygame.draw.rect(screen, (92, 64, 51), (365, 260, 45, 90)) # door
    pygame.draw.circle(screen, (255, 215, 0), (375, 310), 5) # doorknob


    # sun
    pygame.draw.circle(screen, sun_color, (sun_x, sun_y), sun_radius)

    if weather >= 3: # rainy
        rain_alpha = 255
    else:
        if prev_weather >= 3 and rain_alpha > 0:
            rain_alpha -= 2 # rain fades out (i think its pretty cool)
    
    if rain_alpha >= 0:
        rain_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        # draw rain streaks
        for _ in range(200):
            x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            # only draw rain streaks below the clouds
            for cloud in cloud_coords:
                if x > cloud[0] - 60 + (y - 100) * 0.5 + 15 and x < cloud[0] + 60 + (y - 100) * 0.5 and y > cloud[1] + 10:
                    pygame.draw.line(rain_surface, (0, 0, 255, rain_alpha), (x, y), (x + 10, y + 20), 2)
                    break
                # pygame.draw.line(screen, (0, 0, 255), (x, y), (x + 10, y + 20), 2)

        screen.blit(rain_surface, (0, 0))

    # lightning things
    if weather == 4:
        # fire lightning from some random cloud to the ground
        if thunder_this_frame:
            cloud = random.choice(cloud_coords)
            # sticking with line cuz i dont know how to draw a good looking lightning bolt
            pygame.draw.line(screen, (255,154,0), (cloud[0] + random.randint(-70, 70), cloud[1] + 30), (cloud[0] + random.randint(-140, 140), 350), 3)

    # draw clouds
    for cloud in cloud_coords:
        # compound shape - 3 circles with reference to cloud[0] and cloud[1]
        pygame.draw.circle(screen, (255, 255, 255), tuple(cloud), 30)
        pygame.draw.circle(screen, (255, 255, 255), (cloud[0] + 40, cloud[1] + 5), 30)
        pygame.draw.circle(screen, (255, 255, 255), (cloud[0] - 40, cloud[1] + 5), 30)
        cloud[0] += 0.5
        if cloud[0] > WIDTH + 70:
            cloud_coords.remove(cloud)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(120 * speed_multiplier)
    #---------------------------


pygame.quit()