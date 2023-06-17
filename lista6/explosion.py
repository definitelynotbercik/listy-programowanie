import pygame
from supp import import_folder

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.5

        self.image = pygame.image.load("semestr2\\lista6\\graphics\\enemy\\explosion\\1.png")
        self.rect = self.image.get_rect(center = position)

    
    def import_character_assets(self):
        character_path = "semestr2\\lista6\\graphics\\enemy\\explosion\\"
        self.animations = import_folder(character_path)

    
    def animation(self):
        anim = self.animations

        #lopping over animation indexes
        self.frame_index += self.animation_speed
        if self.frame_index >= len(anim):
            self.kill()
        else:
            self.image = anim[int(self.frame_index)].convert_alpha()


    def update(self, x_move):
        self.animation()
        self.rect.x += x_move