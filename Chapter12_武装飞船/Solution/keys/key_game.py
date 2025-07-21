import sys
import pygame
from settings import Settings

class Keygame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Key Game")
    def run_game(self):
        '''开始加载主要游戏'''
        while True:
            self.check_events()
            self.update_screen()
            self.clock.tick(60)
    def check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self.check_keydown_event(event)
    def check_keydown_event(self,event):
        print(event.key)
        if event.key==pygame.K_q:
            sys.exit()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

if __name__=='__main__':
    kg=Keygame()
    kg.run_game()