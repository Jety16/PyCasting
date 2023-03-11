import constants
import pygame
import math
# raycasting algorithm


class Raycasting():

    def __init__(self, player_angle, map_cfg, player_y, player_x, win):
        self.window = win
        self.player_angle = player_angle
        self.map_cfg = map_cfg
        self.player_x = player_x
        self.player_y = player_y

    def _get_square_index(self, target_x, target_y):
        row = int(target_y / self.map_cfg['tile_size'])
        col = int(target_x / self.map_cfg['tile_size'])
        return row * self.map_cfg['map_size'] + col

    def cast_rays(self):
        # Left most angle of FOV
        start_angle = self.player_angle - constants.HALF_FOV

        for ray in range(constants.RAYS):
            for depth in range(self.map_cfg['max_depth']):
                target_x = self.player_x - math.sin(start_angle) * depth
                target_y = self.player_y + math.cos(start_angle) * depth

                square_index = self._get_square_index(target_x, target_y)
                if self.map_cfg['map_structure'][square_index] == '#':
                    wall_depth = 21000 / (depth + 0.001)
                    # Draw 3D projection
                    pygame.draw.rect(self.window, (205, 140, 120),
                        (0 + ray * constants.SCALE,
                        constants.WIN_HEIGHT / 2 - wall_depth / 2,
                        constants.SCALE, wall_depth))
                    break
                pygame.draw.line(self.window,
                    (90, 90, 90),
                    (self.player_x, self.player_y),
                    (target_x, target_y)
                )
            start_angle += constants.STEP_ANGLE
