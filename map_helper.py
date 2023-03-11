from maps.map_cfg import MAP_CFG
import pygame


class Map():
    def __init__(self, win, map_name, player_x, player_y):
        self.window = win
        self.map_name = map_name
        self.map_cfg = self.get_map_cfg(self.map_name)
        self.player_x = player_x
        self.player_y = player_y

    def get_map_cfg(self, map_name):
        return MAP_CFG[map_name]

    def _get_color(self, index, map_structure):
        # check if is a wall or not
        if map_structure[index] == '#':
            return (205, 140, 120)
        else:
            return (9, 90, 90)

    def print_map(self):
        map_size = self.map_cfg['map_size']
        tile_size = self.map_cfg['tile_size'] # offset to make the map not so tiny.
        for row in range(map_size):
            for col in range(map_size):
                # map column loop
                square_index = row * map_size + col
                pygame.draw.rect(self.window,
                    self. _get_color(square_index, self.map_cfg['map_structure']),
                    (col * tile_size, row * tile_size, tile_size, tile_size))
        # player
        pygame.draw.circle(self.window,
            (255, 0, 0), (self.player_x, self.player_y), 4)