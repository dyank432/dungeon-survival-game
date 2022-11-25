import pygame
from settings import *

class Upgrade:
    def __init__(self, player):

        self.display_surface = pygame.display.get_surface()
        self.player = player
        
        self.attr = ['1','2','3']
        self.attribute_nr = len(self.attr)
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

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
            if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_nr - 1:
                self.selection_index += 1
                self.can_move = False 
                self.selection_time = pygame.time.get_ticks()
                print(self.selection_index)

            elif keys[pygame.K_LEFT] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                print(self.selection_index)

            if keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                print(self.selection_index)
    
    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True

    def create_items(self):
        self.item_list = []

        # for item,index in enumerate(range(self.attr)):
        for item, index in enumerate(range(self.attribute_nr)):
            full_width = self.display_surface.get_size()[0]  
            increment = full_width // self.attribute_nr
            left = (item * increment) + (increment - self.width) // 2

            top = self.display_surface.get_size()[1] * 0.1 

            # item = Item(left, top, self.width, self.height, index, self.font)
            item = Item(left, top, self.width, self.height, index, self.font)
            self.item_list.append(item)

    def display(self):
    #    self.display_surface.fill('black')
        self.input()
        self.selection_cooldown()

        for item in self.item_list:
            item.display(self.display_surface, 0, 'TEST', 0, 2, 1)
class Item:
    def __init__(self, l, t, w, h, index, font):
        self.rect = pygame.Rect(l,t,w,h)
        self.index = index
        self.font = font
    
    def display_names(self, surface, name, cost, selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR
        # title
        title_surf = self.font.render(name, False, color)
        title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))
        # cost
        cost_surf = self.font.render(f'{int(cost)}', False, color)
        cost_rect = cost_surf.get_rect(midbottom = self.rect.midbottom - pygame.math.Vector2(0,20))
        # draw
        surface.blit(title_surf, title_rect)
        surface.blit(cost_surf, cost_rect)


    def display(self, surface, selection_num, name, value, max_value, cost):
        if self.index == selection_num:
            pygame.draw.rect(surface, BG_COLOR_SELECTED, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        else:
            pygame.draw.rect(surface, UI_BG_COLOR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)

        self.display_names(surface,name,cost, self.index == selection_num)