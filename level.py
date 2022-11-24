import pygame
from projectile import Projectile 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from ui import UI
from enemy import Enemy

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

		# timer
		self.counting_time = 0

		self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
		self.clock = pygame.time.Clock()
		self.start_time = pygame.time.get_ticks()
		self.paused  = False
		self.counting_time = 0

		# ui
		self.ui = UI()

	def create_map(self):
		for row_index,row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x' or col == 'l' or col == 'r' or col == 't' or col == 'b' or col == 'br' or col == 'bl' or col == 'tr' or col == 'tl':
					Tile((x,y),[self.visible_sprites,self.obstacle_sprites], 'wall', col)
				if col == 'p':
					self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites, self.create_projectile)
				# temp for enemy testing
				if col == 'e':
					Enemy('ghost', (x,y), [self.visible_sprites], self.obstacle_sprites)

	def create_projectile(self):
		Projectile(self.player, [self.visible_sprites] )


	def run(self):
		# update and draw the game
		if not self.paused:
			self.counting_time = pygame.time.get_ticks() - self.start_time
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		self.visible_sprites.enemy_update(self.player)
		self.ui.display(self.player, self.counting_time)

# Center the camera on the player
class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		self.floor_surface = pygame.image.load('./assets/floor.png').convert()
		self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))

	def custom_draw(self,player):
		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# draw the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surface, floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

	def enemy_update(self, player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)