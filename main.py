import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
          
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Dungeon Survival')
        self.clock = pygame.time.Clock()
        self.difficulty_increase = pygame.USEREVENT + 0 
        pygame.time.set_timer(self.difficulty_increase, 15000)
        self.level = Level()
    
    def run(self):
        music_playing = True
        pygame.mixer.music.load(BG_MUSIC)
        pygame.mixer.music.play(-1)

        while True:

            self.screen.fill((97, 48, 0))
            self.level.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_SPACE:
                #         self.level.toggle_menu()
                if event.type == self.difficulty_increase:
                    self.level.difficulty_increase()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        if music_playing:
                            pygame.mixer.music.pause()
                            music_playing = False
                        else:
                            pygame.mixer.music.unpause()
                            music_playing = True

                    if self.level.lost == True:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                self.level = Level()

            pygame.display.update()
            self.clock.tick(FPS)
 
if __name__ == '__main__':
    game = Game()
    game.run()