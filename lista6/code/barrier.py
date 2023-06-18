import pygame

class Barrier(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        """
        Initialize a Barrier object.

        Args:
            position (tuple): The position of the top-left corner of the barrier (x, y).
            size (int): The size of the barrier (width and height).
        """

        self.image = pygame.Surface((size,size))
        self.image.fill((255,0,0))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(topleft = position)

    
    def update(self, x_move):
        """
        Update the barrier's position.

        Args:
            x_move (int): The amount to move the barrier along the x-axis based on the camera movement.
        """
        
        self.rect.x += x_move
