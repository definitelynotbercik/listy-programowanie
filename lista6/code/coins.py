import pygame
from supp import import_folder

class Coin(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        """
        Initialize the Coin object.

        Args:
            position (tuple): The initial position of the coin (x, y).
            size (int): The size of the coin (width and height).
        """

        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = pygame.image.load("semestr2\\lista6\\graphics\\coin\\01.png")
        self.image = pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect(topleft = position)

    
    def import_character_assets(self):
        """
        Import the character assets.

        Loads and stores the coin animation images from the specified folder.
        """

        character_path = "semestr2\\lista6\\graphics\\coin\\"
        self.animations = import_folder(character_path)
    
    
    def animation(self):
        """Animate the coin."""

        anim = self.animations

        # Lopping over animation indexes
        self.frame_index += self.animation_speed
        if self.frame_index >= len(anim):
            self.frame_index = 0

        self.image = anim[int(self.frame_index)].convert_alpha()


    def update(self, x_move):
        """
        Update the coin.

        Args:
            x_move (int): The amount to move the coin along the x-axis based on the camera movement.
        """

        self.animation()
        self.rect.x += x_move
