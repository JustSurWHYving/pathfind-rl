from PIL import Image

class SpriteSheet:
    def __init__(self, image_path, sprite_width=16, sprite_height=16):
        """
        Initializes the SpriteSheet class.

        Args:
            image_path (str): Path to the sprite sheet image.
            sprite_width (int): Width of each sprite in pixels (default: 16).
            sprite_height (int): Height of each sprite in pixels (default: 16).
        """
        self.image_path = image_path
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        try:
            self.image = Image.open(self.image_path)
            self.image.load()  # Ensure image is fully loaded
            self.width, self.height = self.image.size
            self.cols = self.width // self.sprite_width
            self.rows = self.height // self.sprite_height
            self.total_sprites = self.cols * self.rows
        except FileNotFoundError:
            print(f"Error: Image file not found at {self.image_path}")
            self.image = None
            self.width = 0
            self.height = 0
            self.cols = 0
            self.rows = 0
            self.total_sprites = 0
        except Exception as e:
            print(f"Error loading image: {e}")
            self.image = None
            self.width = 0
            self.height = 0
            self.cols = 0
            self.rows = 0
            self.total_sprites = 0

    def get_sprite(self, index):
        """
        Retrieves a specific sprite from the sprite sheet based on its index.

        Args:
            index (int): The index of the sprite to retrieve (starting from 0,
                         left to right, top to bottom).

        Returns:
            PIL.Image.Image or None: The sprite image as a PIL Image object,
                                     or None if the index is out of bounds or
                                     the image failed to load.
        """
        if self.image is None:
            print("Error: Sprite sheet image not loaded.")
            return None

        if not (0 <= index < self.total_sprites):
            print(f"Error: Sprite index {index} out of bounds. "
                  f"Must be between 0 and {self.total_sprites - 1}.")
            return None

        row = index // self.cols
        col = index % self.cols

        left = col * self.sprite_width
        top = row * self.sprite_height
        right = left + self.sprite_width
        bottom = top + self.sprite_height

        try:
            sprite = self.image.crop((left, top, right, bottom))
            return sprite
        except Exception as e:
            print(f"Error cropping sprite: {e}")
            return None

    def get_all_sprites(self):
        """
        Retrieves all sprites from the sprite sheet as a list of PIL Image objects.

        Returns:
            list[PIL.Image.Image] or None: A list of sprite images, or None if
                                            the image failed to load.
        """
        if self.image is None:
            print("Error: Sprite sheet image not loaded.")
            return None

        sprites = []
        for i in range(self.total_sprites):
            sprite = self.get_sprite(i)
            if sprite:
                sprites.append(sprite)
        return sprites
    