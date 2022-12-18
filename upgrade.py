import random
import pygame
from settings import *

class Upgrade:
    def __init__(self, player):

        self.display_surface = pygame.display.get_surface()
        self.player = player
        
        self.attr = ['1','2','3']
        self.attribute_nr = len(self.attr)
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.title_font = pygame.font.Font(UI_FONT, UI_TITLE_FONT_SIZE)

        self.item_selection_list = []
        self.generated_items = False

        # item dimensions
        self.height = self.display_surface.get_size()[1] * 0.8 
        self.width = self.display_surface.get_size()[0] // 4

        self.create_items()

        # selection
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True

    def input(self):
        keys = pygame.key.get_pressed()

        if self.can_move:
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.selection_index < self.attribute_nr - 1:
                self.selection_index += 1
                self.can_move = False 
                self.selection_time = pygame.time.get_ticks()
                # print(self.selection_index)

            elif (keys[pygame.K_LEFT]  or keys[pygame.K_a]) and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                # print(self.selection_index)

            if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                self.generated_items = False
                self.apply_item_upgrade()
                self.player.exp = 0
                self.player.lvlup_exp *= 1.10
                # print(self.selection_index)

    def apply_item_upgrade(self):
        if self.item_list[self.selection_index].name == 'BOOTS OF SPEED' and self.player.speed <= 10:
            self.player.speed += item_data[0]['modifier']
            print(f'curr speed: {self.player.speed}')
        if self.item_list[self.selection_index].name == 'SHARPENED DAGGERS' and self.player.damage <= 25:
            self.player.damage += item_data[1]['modifier']
            print(f'curr damage: {self.player.damage}')
        if self.item_list[self.selection_index].name == 'REINFORCED SHIELD' and self.player.armour <= 25:
            self.player.armour += item_data[2]['modifier']
            print(f'curr armour: {self.player.armour}')
        if self.item_list[self.selection_index].name == 'DURABLE BELT' and self.player.damage <= 500:
            self.player.max_hp += item_data[3]['modifier']            
            self.player.hp += item_data[3]['modifier']
            print(f'curr max hp: {self.player.max_hp}')
        if self.item_list[self.selection_index].name == 'DEXTEROUS GLOVES' and self.player.attack_cooldown >= 100:
            self.player.attack_cooldown -= item_data[4]['modifier']
            print(f'curr attack_speed: {self.player.attack_cooldown}')
        if self.item_list[self.selection_index].name == 'HEALTH POTION':
            self.player.hp = self.player.max_hp
        if self.item_list[self.selection_index].name == 'EXTENDED KNIFETHROWER' and self.player.range <= 2500:
            self.player.range += item_data[6]['modifier']
            print(f'curr range: {self.player.range}')
        if self.item_list[self.selection_index].name == 'QUICKDRAW BACKPACK' and self.player.projectile_speed <= 10:
            self.player.projectile_speed += item_data[7]['modifier']
            print(f'curr projectile_speed: {self.player.projectile_speed}')

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 265:
                self.can_move = True

    def create_items(self):
        self.item_list = []

        for item, index in enumerate(range(self.attribute_nr)):
            full_width = self.display_surface.get_size()[0]  
            increment = full_width // self.attribute_nr
            left = (item * increment) + (increment - self.width) // 2

            top = self.display_surface.get_size()[1] * 0.3 
            bottom = self.display_surface.get_size()[1] - 300 

            item = Item(left, top, self.width, bottom, index, self.font)
            self.item_list.append(item)

    def display(self):
    #    self.display_surface.fill('black')
        self.input()
        self.selection_cooldown()

        # for i in range(6):
        #     print(item_data[i]['description'])

        if (not self.generated_items):
            self.item_selection_list = self.randomize_items()
            # print(self.item_selection_list)

            # print(item_data)
            # print(item_data.keys())

        color = TEXT_COLOR
        # title
        title_surf = self.title_font.render("Select an upgrade (use MOVEMENT KEYS + ENTER/SPACE to select)", False, color)
        title_rect = title_surf.get_rect(topleft = (WIDTH/2 - title_surf.get_width() // 2, 100))  #+ pygame.math.Vector2(0,0))

        pygame.draw.rect(self.display_surface, (0, 0, 0), title_rect)
        self.display_surface.blit(title_surf, (WIDTH/2 - title_surf.get_width() // 2, 100))


        for item in self.item_list:
            ### print(self.item_selection_list)
            ### print(self.item_selection_list[item.index])
            item.display(self.display_surface, self.selection_index, self.item_selection_list[item.index]) #item.index

    def randomize_items(self):
        self.generated_items = True
        return random.sample(item_data, 3)

class Item:
    def __init__(self, l, t, w, h, index, font):
        self.rect = pygame.Rect(l,t,w,h)
        self.index = index
        self.font = font
        self.name = ''

    def display_items(self, surface, name, desc, image, selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        self.name = name
        # name
        name_surf = self.font.render(name, False, color)
        name_rect = name_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,35))

        # description
        desc_surf = self.font.render(desc, False, color)
        desc_rect = desc_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,300))

        # item image
        picture = pygame.image.load(f'./assets/items/{image}.png').convert_alpha()
        image = picture = pygame.transform.scale(picture, (128, 128))
        image_rect = image.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,100))

        # draw
        display_surface = pygame.display.get_surface()
        pygame.draw.rect(display_surface, TEXT_COLOR_SELECTED, image_rect, 4, 3)
        surface.blit(name_surf, name_rect)
        surface.blit(desc_surf, desc_rect)
        surface.blit(image, image_rect)

        # select
        if selected:
            select_surf = self.font.render("SELECT", False, color)
            select_rect = select_surf.get_rect(midbottom = self.rect.midbottom - pygame.math.Vector2(0,20))
            surface.blit(select_surf, select_rect)

    def display(self, surface, selection_num, item):
        if self.index == selection_num:
            pygame.draw.rect(surface, BG_COLOR_SELECTED, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        else:
            pygame.draw.rect(surface, UI_BG_COLOR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)

        self.display_items(surface, item['name'], item['description'], item['image'], self.index == selection_num)
    
