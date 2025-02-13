"""
The `GameGrid` class is responsible for managing the game grid, which is a 2D grid of tiles. It handles the initialization of the Pygame window, the creation of an empty grid, and the drawing of the grid on the screen.

The class has the following attributes:
- `window_size`: the size of the Pygame window
- `grid_size`: the size of the game grid (both width and height)
- `tile_size`: the size of each tile in the grid
- `tiles`: a dictionary of tile sprites loaded from the "assets/" directory
- `screen`: the Pygame window surface

The `draw_grid()` method is responsible for rendering the game grid on the screen. It iterates over the grid and draws the corresponding tile sprite for each non-zero tile ID.
"""
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
