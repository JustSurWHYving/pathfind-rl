import pygame

from game.grid import GameGrid
from utils.getsprites import SpriteMaker

def spritemaker():
    sprite_sheets_path = "assets/"
    sprite_maker = SpriteMaker(sprite_sheets_path)

    sprite_maker.process_all_sheets()
    print(f"Sprites extracted from {sprite_sheets_path} and saved")
    sprite_maker.load_sprites()
    print("Sprites indexed")
    sprite_maker.save_sprite_indices()
    print("Sprite indices saved")

def gameloop():
    # Initialize the game grid
    pygame.init()
    game_grid = GameGrid((800, 800), 10, 16) # Initialize game grid (800x800 window, 50x50 grid, 16x16 tiles)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        game_grid.screen.fill((0, 0, 0))
        # Draw the grid
        game_grid.draw_grid()
        # Update the display
        pygame.display.flip

    pygame.quit()

# Get the sprite sheet images
if __name__ == "__main__":
    # Create the sprites from the sprite sheets
    spritemaker()

