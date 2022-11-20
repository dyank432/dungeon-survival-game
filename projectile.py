import pygame
import math
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)

        self.display_surface = pygame.display.get_surface()

        self.speed = 6
        self.mx = (pygame.mouse.get_pos()[0] - WIDTH / 2)  
        self.my = -(pygame.mouse.get_pos()[1] - HEIGHT /2)
        self.angle = (math.atan2(self.my, self.mx))

        picture = pygame.image.load('./assets/weapons/dagger.png').convert_alpha()
        picture = pygame.transform.scale(picture, (48, 48))
        self.degrees = math.degrees(self.angle)
        self.image = pygame.transform.rotate(picture, self.degrees)
        self.rect = self.image.get_rect()

        self.rect.x = player.rect.centerx - 24
        self.rect.y = player.rect.centery - 24

        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)

    def update(self):  

        # kill projectile when they reach the wall boundaries
        if self.rect.left < TILESIZE or self.rect.right > WIDTH - TILESIZE + 20 or self.rect.top < TILESIZE - 45 or self.rect.bottom > 1280 - TILESIZE + 45:
            self.kill()

        # aiming line
        self.pos = pygame.mouse.get_pos()
        # pygame.draw.line(self.display_surface, (255,255,255), (WIDTH / 2, HEIGHT /2), (self.pos), 3)

        # crosshair
        picture = pygame.image.load('./assets/crosshair.png').convert_alpha()
        picture = pygame.transform.scale(picture, (64, 64))
        self.display_surface.blit(picture, (self.pos[0] - 32, self.pos[1] - 32))

        self.rect.x += self.dx
        self.rect.y += self.dy