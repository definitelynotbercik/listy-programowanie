import pygame

class Barrier(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill((255,0,0))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(topleft = position)

    
    def update(self, x_move):
        self.rect.x += x_move