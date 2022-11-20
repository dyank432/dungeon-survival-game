import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame = 0
        self.animation_speed = 0.075
        self.direction = pygame.math.Vector2()

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.detect_collision('x')
        self.hitbox.y += self.direction.y * speed
        self.detect_collision('y')
        self.rect.center = self.hitbox.center
        
        # self.rect.center += self.direction * speed

    #static obstacle collision
    def detect_collision(self, direction):
        if direction == 'x':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # right movement
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # left movement
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'y':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # down movement
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # up movement
                        self.hitbox.top = sprite.hitbox.bottom