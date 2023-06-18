import pygame
from supp import import_folder

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        """
        Initialize the Explosion object.

        Args:
            position (tuple): The initial position of the explosion (x, y).
        """

        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.5

        self.image = pygame.image.load("semestr2\\lista6\\graphics\\enemy\\explosion\\1.png")
        self.rect = self.image.get_rect(center = position)

    
    def import_character_assets(self):
        """
        Import the character assets.

        Loads and stores the explosion animation images from the specified folder.
        """

        character_path = "semestr2\\lista6\\graphics\\enemy\\explosion\\"
        self.animations = import_folder(character_path)

    
    def animation(self):
        """Animate the explosion."""

        anim = self.animations

        # Lopping over animation indexes
        self.frame_index += self.animation_speed
        if self.frame_index >= len(anim):
            self.kill()
        else:
            self.image = anim[int(self.frame_index)].convert_alpha()


    def update(self, x_move):
        """
        Update the explosion.

        Args:
            x_move (int): The amount to move the explosion along the x-axis based on the camera movement.
        """
        
        self.animation()
        self.rect.x += x_move
