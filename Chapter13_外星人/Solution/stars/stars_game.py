import sys
import pygame
from settings import Settings
from star import Star

class StarsGame:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Stars')
        self.stars=pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type== pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key==pygame.K_q:
            sys.exit()

    def _create_stars(self):
        """创建一个星星行"""
        star=Star(self)
        star_width,star_height=star.rect.size
        current_x,current_y=star_width,star_height
        while current_y<(self.settings.screen_height-3*star_height):
            while current_x<self.settings.screen_width-2*star_width:
                self._create_star(current_x,current_y)
                current_x+=2*star_width

            #添加完一行星星后，重置current_x并增加current_y
            current_x=star_width
            current_y+=2*star_height

    def _create_star(self,x_position,y_postion):
        #创建一行星星放在当前行中
        new_star=Star(self)
        #new_star.x=x_position
        new_star.rect.x=x_position
        new_star.rect.y=y_postion

        self.stars.add(new_star)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    stars_game=StarsGame()
    stars_game.run_game()
