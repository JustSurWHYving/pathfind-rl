"""
Provides a SpriteMaker class to process sprite sheets and save individual sprites.

The SpriteMaker class takes an input folder containing sprite sheet images, and an optional sprite width and height. It processes all sprite sheets in the input folder, extracts individual sprites, and saves them to an output folder. The class also provides methods to load the sprites and save the sprite indices to CSV and TXT files.
"""
import os
import csv
import pygame

from PIL import Image

class SpriteMaker:
    def __init__(self, input_folder, sprite_width=16, sprite_height=16):
        """
        Initializes the SpriteSheet class.

        Args:
            input_folder (str): Path to folder containing sprite sheet images
            sprite_width (int): Width of each sprite in pixels (default: 16)
            sprite_height (int): Height of each sprite in pixels (default: 16)
        """
        self.input_folder = input_folder
        self.output_folder = os.path.join(self.input_folder, "sprites")

        # Create output folder if it doesn't exist
        os.makedirs(self.output_folder, exist_ok=True)

        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.tiles = {}
        
    def process_all_sheets(self):
        """Process all sprite sheets in the input folder"""
        for filename in os.listdir(self.input_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(self.input_folder, filename)
                self.process_single_sheet(image_path, filename)

    def process_single_sheet(self, image_path, original_filename):
        """Process a single sprite sheet and save individual sprites"""
        try:
            image = Image.open(image_path)
            width, height = image.size
            cols = width // self.sprite_width
            rows = height // self.sprite_height
            
            # Create subfolder for this sprite sheet
            sheet_name = os.path.splitext(original_filename)[0]
            sheet_output_folder = os.path.join(self.output_folder, sheet_name)
            os.makedirs(sheet_output_folder, exist_ok=True)
            
            # Extract and save individual sprites
            for row in range(rows):
                for col in range(cols):
                    left = col * self.sprite_width
                    top = row * self.sprite_height
                    right = left + self.sprite_width
                    bottom = top + self.sprite_height
                    
                    sprite = image.crop((left, top, right, bottom))
                    sprite_filename = f"sprite_{row}_{col}.png"
                    sprite_path = os.path.join(sheet_output_folder, sprite_filename)
                    sprite.save(sprite_path)
                    
        except Exception as e:
            print(f"Error processing {original_filename}: {e}")

    def load_sprites(self):
        tiles = self.tiles
        index = 0
        for folder in os.listdir(self.output_folder):
            folder_path = os.path.join(self.output_folder, folder)
            if os.path.isdir(folder_path):
                for sprite in os.listdir(folder_path):
                    if sprite.endswith('.png'):
                        sprite_path = os.path.join(folder_path, sprite)
                        tiles[index] = sprite_path
                        index += 1
        return tiles
        
    def save_sprite_indices(self):
        # Save as a CSV file
        csv_path = os.path.join(self.output_folder, 'sprite_indices.csv')
        with open(csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Index', 'Sprite Path'])
            for sprite_id, sprite in self.tiles.items():
                writer.writerow([sprite_id, sprite])

        # Save as a TXT file
        txt_path = os.path.join(self.output_folder, 'sprite_indices.txt')
        with open(txt_path, 'w') as txtfile:
            for sprite_id, sprite in self.tiles.items():
                txtfile.write(f'{sprite_id}: {sprite}\n')