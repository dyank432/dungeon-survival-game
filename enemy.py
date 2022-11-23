import pygame
from settings import *
from entity import Entity
from support import import_folder

class Enemy(Entity):
    def __init__(self, name, pos, groups, obstacle_sprites):
        super().__init__(groups)

        self.sprite_type = 'enemy'
        picture = pygame.image.load('./assets/enemies/ghost_0.png').convert_alpha()
        self.image = picture = pygame.transform.scale(picture, (64, 64))

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstacle_sprites = obstacle_sprites

        self.animation_speed = 0.040

        self.import_enemy_assets()


    def import_enemy_assets(self):
        player_path = './assets/enemies/'
        self.animations = {
            'walk': []
        }

        for animation in self.animations.keys():
            full_path = player_path + animation
            self.animations[animation] = import_folder(full_path)

        # stats
        # todo: based on monster name
        self.speed = 3
    
    def get_status(self, player):
        distance = self.get_player_position(player)[0]
        self.direction = self.get_player_position(player)[1]

    def get_player_position(self, player):
        enemy_vector = pygame.math.Vector2(self.rect.center)
        player_vector =  pygame.math.Vector2(player.rect.center)
        distance = (player_vector - enemy_vector).magnitude()

        if distance > 0:
            direction = (player_vector - enemy_vector).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)
    
    def animate(self):
        animation = self.animations['walk']

        # loop through the animation
        self.frame += self.animation_speed
        if self.frame >= len(animation):
            self.frame = 0

        # set image to current frame
        self.image = animation[int(self.frame)]

    def update(self):
        self.move(self.speed)

    def enemy_update(self, player):
        self.get_status(player)
        self.animate()
