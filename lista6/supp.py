import os
import pygame

def import_folder(path):
    surface_list = []
    
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + "\\" + image
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)
    
    return surface_list

