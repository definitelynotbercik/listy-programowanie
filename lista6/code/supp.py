import os
import pygame
from settings import WIDTH

def import_folder(path):
    """
    Loads all images from a folder and returns a list of surfaces.

    Args:
        path (str): The path to the folder containing the images.

    Returns:
        list: A list of pygame.Surface objects representing the loaded images.
    """

    surface_list = []
    
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + "\\" + image
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)
    
    return surface_list


def display_text(surface, text, position, font, color):
    """
    Displays text on a surface with a specified font and color.

    Args:
        surface (pygame.Surface): The surface to display the text on.
        text (str): The text to be displayed.
        position (tuple): The position (x, y) where the text should be rendered.
        font (pygame.font.Font): The font used for rendering the text.
        color (tuple): The color of the text in RGB format.
    """

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
