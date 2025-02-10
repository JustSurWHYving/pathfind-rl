from utils.getsprites import SpriteSheet

# Get the sprite sheet images
if __name__ == "__main__":
    sprite_sheet_path = "path/to/your/sprite_sheet.png"
    sprite_sheet = SpriteSheet(sprite_sheet_path)

    if sprite_sheet.image:
        # Get a specific sprite (e.g., the 5th sprite)
        sprite_index = 4
        sprite = sprite_sheet.get_sprite(sprite_index)
        if sprite:
            sprite.save(f"sprite_{sprite_index}.png")
            print(f"Sprite at index {sprite_index} saved as sprite_{sprite_index}.png")

        # Get all sprites
        all_sprites = sprite_sheet.get_all_sprites()
        if all_sprites:
            for i, sprite in enumerate(all_sprites):
                sprite.save(f"all_sprite_{i}.png")
            print(f"All {len(all_sprites)} sprites saved.")
