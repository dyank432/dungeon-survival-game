import pygame
from settings import *

class UI:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.timerFont = pygame.font.Font(UI_FONT, 24)

        # bars
        self.hp_bar_rect = pygame.Rect(10, 10, BAR_WIDTH, BAR_HEIGHT)
        self.exp_bar_rect = pygame.Rect(10, 40, BAR_WIDTH, BAR_HEIGHT)

    def draw_bar(self, current, max, bg_rect, color):
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # convert value to correct hp bar ratio
        ratio = current / max
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
    
    def draw_exp_text(self, exp):
        text_surface = self.font.render("XP: " + str(int(exp)),False,TEXT_COLOR)
        text_rect = text_surface.get_rect(topleft = (15,43)) 

        self.display_surface.blit(text_surface, text_rect)

    def draw_hp_text(self, hp):
        text_surface = self.font.render("HP: " + str(int(hp)),False,TEXT_COLOR)
        text_rect = text_surface.get_rect(topleft = (15,13)) 

        self.display_surface.blit(text_surface, text_rect)

    def draw_timer_text(self, time):
        # change milliseconds into minutes, seconds
        counting_minutes = str(time//60000).zfill(2)
        counting_seconds = str( (time%60000)//1000 ).zfill(2)

        counting_string = "%s:%s" % (counting_minutes, counting_seconds)

        text_surface = self.timerFont.render(str(counting_string),False,TEXT_COLOR)
        text_rect = text_surface.get_rect(topleft = (WIDTH/2 - 25, 0)) 

        pygame.draw.rect(self.display_surface, (UI_BORDER_COLOR), text_rect)
        self.display_surface.blit(text_surface, text_rect)

    def display(self, player, time):
        self.draw_bar(player.hp, player.max_hp, self.hp_bar_rect, UI_HP_COLOR)
        self.draw_bar(player.exp, player.lvlup_exp, self.exp_bar_rect, UI_EXP_COLOR)

        self.draw_exp_text(player.exp)
        self.draw_hp_text(player.hp)
        self.draw_timer_text(time)