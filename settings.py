import pygame

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)

PLAYER_HIT_SOUND = pygame.mixer.Sound("./assets/sounds/player_hit.ogg")
ENEMY_HIT_SOUND = pygame.mixer.Sound("./assets/sounds/enemy_hit.ogg")
THROW_SOUND = pygame.mixer.Sound("./assets/sounds/throw.ogg")
STEP_SOUND = pygame.mixer.Sound("./assets/sounds/throw.ogg")

BG_MUSIC = "./assets/sounds/bg_music.ogg"

# volume
pygame.mixer.music.set_volume(0.05)
PLAYER_HIT_SOUND.set_volume(0.15)
ENEMY_HIT_SOUND.set_volume(0.05)
THROW_SOUND.set_volume(0.06)
STEP_SOUND.set_volume(0.06)

# game setup
WIDTH    = 1280 
HEIGHT   = 720
FPS      = 60
TILESIZE = 64
 
# ui
BAR_HEIGHT = 25
BAR_WIDTH = 250
UI_FONT = './assets/fonts/Retro Gaming.ttf'
UI_FONT_SIZE = 15
UI_TITLE_FONT_SIZE = 22

# colors
TEXT_COLOR = '#EEEEEE' 
UI_BG_COLOR = '#222222' 
UI_BORDER_COLOR = '#111111' 
UI_HP_COLOR = (181, 4, 4) 
UI_EXP_COLOR = (0, 161, 37) 

BG_COLOR_SELECTED = '#EEEEEE'
TEXT_COLOR_SELECTED = (0,0,0)

# weapon data
weapon_data = {
    'projectile': { 'cooldown': 100, 'damage': 5 }
}

item_data = [
    { 'name': 'BOOTS OF SPEED', 'modifier': 1.025, 'description': "Increase base movement speed.", 'value': 0, 'max_value': 10, 'image': 'boots'},
    { 'name': 'SHARPENED DAGGERS',  'modifier': 2, 'description': "Increases weapon damage.", 'value': 0, 'max_value': 10, 'image': 'dagger'},
    { 'name': 'REINFORCED SHIELD',  'modifier': 1, 'description': "Reduces damage taken.", 'value': 0, 'max_value': 10, 'image': 'shield'},
    { 'name': 'DURABLE BELT', 'modifier': 20, 'description': "Increase maximum health.", 'value': 0, 'max_value': 10, 'image': 'belt'},
    { 'name': 'DEXTEROUS GLOVES', 'modifier': 20, 'description': "Increases attack speed.", 'value': 0, 'max_value': 10, 'image': 'gloves'},
    { 'name': 'HEALTH POTION', 'modifier': 1000, 'description': "fully restores your health.", 'value': 0, 'max_value': 10, 'image': 'potion'},
    { 'name': 'SNIPER CROSSBOW', 'modifier': 75, 'description': "Increases attack range.", 'value': 0, 'max_value': 10, 'image': 'crossbow'},
    { 'name': 'QUICKDRAW BACKPACK', 'modifier': 0.25, 'description': "Increases projectile speed.", 'value': 0, 'max_value': 10, 'image': 'backpack'}
]

# enemy data
enemy_data = {
    'ghost': { 'hp': 5, 'exp': 5, 'damage': 5, 'speed': 3 }
}


# 20x20 
WORLD_MAP = [
['tl','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','tr'],
['l','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','r'],
['l','e',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','e',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r'],
['bl','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','br'],
]