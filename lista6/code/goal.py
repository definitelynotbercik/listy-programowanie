import pygame
from supp import import_folder

class Goal(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        """
        Initialize the Goal object.

        Args:
            position (tuple): The initial position of the goal (x, y).
            size (int): The size of the goal image.
        """

        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = pygame.image.load("semestr2\\lista6\\graphics\\key\\1.png")
        self.image = pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect(topleft = position)


    def import_character_assets(self):
        """
        Import the character assets.

        Loads and stores the goal animation images from the specified folder.
        """

        character_path = "semestr2\\lista6\\graphics\\key\\"
        self.animations = import_folder(character_path)


    def animation(self):
        """Animate the goal."""

        anim = self.animations

        #lopping over animation indexes
        self.frame_index += self.animation_speed
        if self.frame_index >= len(anim):
            self.frame_index = 0

        self.image = anim[int(self.frame_index)].convert_alpha()

    
    def update(self, x_move):
        """
        Update the goal.

        Args:
            x_move (int): The amount to move the goal along the x-axis based on the camera movement.
        """

        self.animation()
        self.rect.x += x_move
