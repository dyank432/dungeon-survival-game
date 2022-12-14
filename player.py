import pygame
from projectile import Projectile
from settings import *
from support import import_folder
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, create_projectile):
        super().__init__(groups)
        picture = pygame.image.load('./assets/player/player_1.png').convert_alpha()
        self.image = pygame.transform.scale(picture, (64, 64))

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-50)

        self.speed = 5

        self.attacking = False
        self.attack_cooldown = 500
        self.attack_time = None

        self.obstacle_sprites = obstacle_sprites

        self.import_player_assets()

        #stats
        self.max_hp = 100
        self.hp = 100
        self.armour = 0
        self.damage = 5
        self.range = 700
        self.projectile_speed = 6

        self.lvlup_exp = 100
        self.exp = 0

        # projectiles
        self.projectiles = []
        self.create_projectile = create_projectile

        # damage timer
        self.vulnerable = True
        self.hit_time = None
        self.invulnerability_duration = 500

    def import_player_assets(self):
        player_path = './assets/player/'
        self.animations = {
            'idle': [],
            'walk': []
        }

        for animation in self.animations.keys():
            full_path = player_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()

        # movement
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'walk'
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'walk'
        else:
            self.direction.y = 0
            self.status = 'idle'

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'walk'
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'walk'
        else:
            self.direction.x = 0

        # attack
        if not self.attacking:
            self.attacking = True
            self.create_projectile()
            pygame.mixer.Sound.play(THROW_SOUND)
            self.attack_time = pygame.time.get_ticks()
            
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

        if not self.vulnerable:
            if current_time - self.hit_time >= self.invulnerability_duration:
                self.vulnerable = True

    def animate(self):
        animation = self.animations[self.status]

        # loop through the animation
        self.frame += self.animation_speed
        if self.frame >= len(animation):
            self.frame = 0

        # set image to current frame
        self.image = animation[int(self.frame)]

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def get_total_damage(self):
        base_dmg = self.damage
        # add buff damage from items
        return base_dmg

    def update(self):
        self.input()
        self.cooldowns()
        self.animate()
        self.move(self.speed)
