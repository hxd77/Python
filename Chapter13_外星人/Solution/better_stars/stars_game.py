from settings import Settings
from star import Star
import pygame
import sys
from random import randint

class StarsGame:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings = Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.stars=pygame.sprite.Group()
        pygame.display.set_caption('Stars')
        self._create_stars()

    def run_game(self):
        while True:
            self._check_event()
            self._update_screen()
            self.clock.tick(60)

    def _check_event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_event(event)

    def _check_keydown_event(self,event):
        if event.key==pygame.K_q:
            sys.exit()

    def _create_stars(self):
        star=Star(self)
        star_width,star_height=star.rect.size
        current_x,current_y=star_width,star_height
        while current_y<self.settings.screen_height-3*star_height:
            while current_x<self.settings.screen_width-2*star_width:
                self._create_star(current_x,current_y)
                current_x+=2*star_width

            current_x=star_width
            current_y+=2*star_height

    def _create_star(self,x_position,y_position):
        new_star = Star(self)
        new_star.rect.x=x_position+self._get_star_offset()
        new_star.rect.y=y_position+self._get_star_offset()
        self.stars.add(new_star)

    def _get_star_offset(self):
        """返回星星的随机位置"""
        offset_size=15
        return randint(-1*offset_size,offset_size)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__=='__main__':
    stars_game = StarsGame()
    stars_game.run_game()