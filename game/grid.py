import os
import pygame

from utils.getsprites import SpriteMaker

class GameGrid:
    def __init__(self, window_size, grid_size, tile_size=16):
        self.window_size = window_size
        self.grid_size = grid_size
        self.tile_size = tile_size
        self.tiles = SpriteMaker("assets/").tiles
        
        # Initialize Pygame window
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Pathfind-RL")
        
        # Initialize empty grid
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        
    def draw_grid(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                tile_id = self.grid[row][col]
                if tile_id in self.tiles:
                    self.screen.blit(
                        self.tiles[tile_id],
                        (col * self.tile_size, row * self.tile_size)
                    )
