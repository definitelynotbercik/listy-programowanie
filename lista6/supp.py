import os
import pygame
from settings import WIDTH

def import_folder(path):
    surface_list = []
    
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + "\\" + image
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)
    
    return surface_list


def display_text(surface, text, position, font, color):
    coll = [word.split(" ") for word in text.splitlines()]
    space = font.size(" ")[0]
    x, y = position
    
    for lines in coll:
        for words in lines:
            word_surface = font.render(words, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= WIDTH:
                x = position[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = position[0]
        y += word_height
