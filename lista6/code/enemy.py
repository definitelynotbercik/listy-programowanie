import pygame
import random
from supp import import_folder

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        """
        Initialize the Enemy object.

        Args:
            position (tuple): The initial position of the enemy (x, y).
        """

        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.speed = random.randint(3,5)
        self.image = pygame.image.load("semestr2\\lista6\\graphics\\enemy\\run\\Run 01.png")
        self.rect = self.image.get_rect(topleft = position)


    def import_character_assets(self):
        """
        Import the character assets.

        Loads and stores the enemy animation images from the specified folder.
        """

        character_path = "semestr2\\lista6\\graphics\\enemy\\run\\"
        self.animations = import_folder(character_path)


    def animation(self):
        """Animate the enemy."""

        anim = self.animations

        # Lopping over animation indexes
        self.frame_index += self.animation_speed
        if self.frame_index >= len(anim):
            self.frame_index = 0

        image = anim[int(self.frame_index)].convert_alpha()

        if self.speed <= -1:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)

    
    def movement(self):
        """Move the enemy horizontally based on its speed."""

        self.rect.x += self.speed


    def reverse(self):
        """Reverse the direction of the enemy's movement."""

        self.speed *= -1


    def update(self, x_move):
        """
        Update the enemy.

        Args:
            x_move (int): The amount to move the enemy along the x-axis based on the camera movement.
        """

        self.animation()
        self.rect.x += x_move
        self.movement()
