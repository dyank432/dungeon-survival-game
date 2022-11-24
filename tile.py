import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, orientation):
        super().__init__(groups)
        # self.image = pygame.image.load('./assets/wall_1.png')
        if orientation == 'x':
            loadPic = 'wall_1'
        if orientation == 't':
            loadPic = 'wall_3'
        if orientation == 'b':
            loadPic = 'wall_6'
        if orientation == 'l':
            loadPic = 'wall_4'
        if orientation == 'r':
            loadPic = 'wall_5'

        if orientation == 'br':
            loadPic = 'wall_9'
        if orientation == 'bl':
            loadPic = 'wall_8'
        if orientation == 'tr':
            loadPic = 'wall_2'
        if orientation == 'tl':
            loadPic = 'wall_7'

        picture = pygame.image.load(f'./assets/wall/{loadPic}.png').convert_alpha()
        self.image = picture = pygame.transform.scale(picture, (64, 64))

        self.sprite_type = sprite_type
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
