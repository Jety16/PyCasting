import math
import sys
import pygame
from map_helper import Map
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

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # Print 2d Map
    game_map = Map(window, 'intro', player_x, player_y)
    game_map.print_map()
    pygame.display.flip()  # Update Display

    # set FPS
    clock.tick(30)
