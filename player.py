import pygame
from projectile import Projectile
from settings import *
from support import import_folder
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, create_projectile):
        super().__init__(groups)
        # self.image = pygame.image.load('./assets/player_1.png').convert_alpha()
        picture = pygame.image.load('./assets/player/player_1.png').convert_alpha()
        self.image = picture = pygame.transform.scale(picture, (64, 64))

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-50)

        # self.direction = pygame.math.Vector2()
        self.speed = 5

        self.attacking = False
        self.attack_cooldown = 500
        self.attack_time = None

        self.obstacle_sprites = obstacle_sprites

        self.import_player_assets()
        # self.status = 'idle'
        # self.frame = 0
        # self.animation_speed = 0.075

        #stats
        self.max_hp = 100
        self.hp = 100

        self.lvlup_exp = 100
        self.exp = 10 # to visualize (should start at 0)

        self.damage = 5
        
        # projectiles (experimental)
        self.projectiles = []
        self.create_projectile = create_projectile

    def import_player_assets(self):
        player_path = './assets/player/'
        self.animations = {
            'idle': [],
            'walk': []
        }

        for animation in self.animations.keys():
            full_path = player_path + animation
            self.animations[animation] = import_folder(full_path)
        # print(self.animations)

    def input(self):
        keys = pygame.key.get_pressed()

        # movement
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'walk'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'walk'
        else:
            self.direction.y = 0
            self.status = 'idle'

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'walk'
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'walk'
        else:
            self.direction.x = 0
            # self.status = 'idle'

        # if keys[pygame.K_SPACE]:
        #     self.projectiles.append(projectile(self.rect.centerx, self.rect.centery, self.visible_sprites))

        # attack
        if not self.attacking:
            self.attacking = True
            self.create_projectile()
            self.attack_time = pygame.time.get_ticks()

    def get_status(self):
        pass

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def animate(self):
        animation = self.animations[self.status]

        # loop through the animation
        self.frame += self.animation_speed
        if self.frame >= len(animation):
            self.frame = 0

        # set image to current frame
        self.image = animation[int(self.frame)]

    def get_total_damage(self):
        base_dmg = self.damage
        # add buff damage from items
        return base_dmg

    def update(self):
        self.input()
        self.cooldowns()
        self.animate()
        self.move(self.speed)
