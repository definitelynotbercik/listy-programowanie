import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size, type):
        super().__init__()
        if type == "filler":
            self.image = pygame.image.load("semestr2\\lista6\\graphics\\terrain\\filler.png")
        elif type == "grass":
            self.image = pygame.image.load("semestr2\\lista6\\graphics\\terrain\\grass.png")
        pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect(topleft = position)

    def update(self, x_move):
        self.rect.x += x_move