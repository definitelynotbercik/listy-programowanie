import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size, type):
        """
        Initializes the Tile class.

        Args:
            position (tuple): The position of the tile (x, y).
            size (int): The size of the tile (width and height).
            type (str): The type of the tile ("filler" or "grass").
        """

        super().__init__()
        if type == "filler":
            self.image = pygame.image.load("semestr2\\lista6\\graphics\\terrain\\filler.png")
        elif type == "grass":
            self.image = pygame.image.load("semestr2\\lista6\\graphics\\terrain\\grass.png")
        pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect(topleft = position)

    def update(self, x_move):
        """
        Updates the tile's position.

        Args:
            x_move (int): The amount to move the tile along the x-axis based on the camera movement.
        """
        self.rect.x += x_move
        