import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type):
        super().__init__(groups)
        # self.image = pygame.image.load('./assets/wall_1.png')
        picture = pygame.image.load('./assets/wall_1.png').convert_alpha()
        self.image = picture = pygame.transform.scale(picture, (64, 64))

        self.sprite_type = sprite_type
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
