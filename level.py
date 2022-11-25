import pygame
from projectile import Projectile 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from ui import UI
from enemy import Enemy
from upgrade import Upgrade

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()
		self.game_paused = False

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# attack sprites
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()

		self.player_sprites = pygame.sprite.Group()
		self.enemy_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

		# timer
		self.counting_time = 0

		self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
		self.clock = pygame.time.Clock()
		self.start_time = pygame.time.get_ticks()
		self.counting_time = 0

		# ui
		self.ui = UI()
		self.upgrade = Upgrade(self.player)

	def create_map(self):
		for row_index,row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x' or col == 'l' or col == 'r' or col == 't' or col == 'b' or col == 'br' or col == 'bl' or col == 'tr' or col == 'tl':
					Tile((x,y),[self.visible_sprites,self.obstacle_sprites], 'wall', col)
				if col == 'p':
					self.player = Player((x,y), [self.visible_sprites, self.player_sprites], self.obstacle_sprites, self.create_projectile)
				# temp for enemy testing
				if col == 'e':
					Enemy('ghost', (x,y), [self.visible_sprites, self.attackable_sprites, self.enemy_sprites], self.obstacle_sprites, self.damage_player, self.add_xp)

	def create_projectile(self):
		Projectile(self.player, [self.visible_sprites, self.attack_sprites] )

	def player_attack_logic(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collided_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
				if collided_sprites:
					for collision in collided_sprites:
						if collision.sprite_type == 'enemy':
							collision.get_damage(self.player, attack_sprite.sprite_type)

	def detect_player_collision(self):
		for enemy in self.enemy_sprites:
			collided_sprites = pygame.sprite.spritecollide(enemy, self.player_sprites, False)
			if collided_sprites:
				enemy.damage_player(enemy.damage)

	def damage_player(self, amt):
		if self.player.vulnerable:
			if self.player.hp >= 0:
				self.player.hp -= amt
			self.player.vulnerable = False
			self.player.hit_time = pygame.time.get_ticks()

	def add_xp(self, amt):
		self.player.exp += amt

	def toggle_menu(self):
		self.game_paused = not self.game_paused

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.ui.display(self.player, self.counting_time)

		if self.game_paused:
			self.upgrade.display()
		# if not self.paused
		else:
			self.counting_time = pygame.time.get_ticks() - self.start_time
			self.visible_sprites.update()
			self.visible_sprites.enemy_update(self.player)
			self.player_attack_logic()
			self.detect_player_collision()

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