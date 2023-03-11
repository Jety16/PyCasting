import math
import sys
import pygame
from map_helper import Map
from raycasting import Raycasting
import constants


# Init pygame
pygame.init()

# Create Window
window = pygame.display.set_mode(
    (constants.WIN_WIDTH, constants.WIN_HEIGHT))
pygame.display.set_caption(constants.WIN_TITLE)

# Init timer
clock = pygame.time.Clock()

# Remove after testing
player_x = 135
player_y = 40
player_angle = math.pi

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # Floor
    pygame.draw.rect(window, (0, 40, 40),
        (0, constants.WIN_HEIGHT / 2,
        constants.WIN_WIDTH, constants.WIN_HEIGHT))

    # Sky
    pygame.draw.rect(window, (50, 30, 30),
        (0, -constants.WIN_HEIGHT / 2,
        constants.WIN_WIDTH, constants.WIN_HEIGHT))

    # Print 2d Map
    game_map = Map(window, 'intro', player_x, player_y)
    game_map.print_map()

    # RayCasting
    raycasting = Raycasting(
        player_angle,
        game_map.get_map_cfg(),
        player_y,
        player_x,
        window)

    raycasting.cast_rays()

    # controller
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_angle -= 0.09
    if keys[pygame.K_RIGHT]:
        player_angle += 0.09
    if keys[pygame.K_UP]:
        player_x += -math.sin(player_angle)
        player_y += math.cos(player_angle)
    if keys[pygame.K_DOWN]:
        player_x -= -math.sin(player_angle)
        player_y -= math.cos(player_angle)

    pygame.display.flip()  # Update Display

    # set FPS
    clock.tick(30)
