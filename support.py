import pygame
from os import walk

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image

            picture = pygame.image.load(full_path).convert_alpha()
            image_surface = picture = pygame.transform.scale(picture, (64, 64))

            surface_list.append(image_surface)

    return surface_list