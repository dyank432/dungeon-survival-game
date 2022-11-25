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

# colors
TEXT_COLOR = '#EEEEEE' 
UI_BG_COLOR = '#222222' 
UI_BORDER_COLOR = '#111111' 
UI_HP_COLOR = (181, 4, 4) 
UI_EXP_COLOR = (0, 161, 37) 

BG_COLOR_SELECTED = '#EEEEEE'
TEXT_COLOR_SELECTED = (0,170,0)

# weapon data
weapon_data = {
    'projectile': { 'cooldown': 100, 'damage': 5 }
}
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