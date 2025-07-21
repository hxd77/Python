import sys
import pygame
from pygame.sprite import Sprite
from settings import Settings
from raindrop import Raindrop

class RaindropsGame:
    def __init__(self):
        #初始化游戏并创建游戏资源
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Raindrops')

        self.raindrops=pygame.sprite.Group()
        self._create_drops()

    def run_game(self):
        """开始游戏循环"""
        while True:
            #侦听键盘和鼠标事件
            self._check_events()
            self.raindrops.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """响应鼠标和键盘事件"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """响应按键按下事件"""
        if event.key==pygame.K_q:
            sys.exit()

    def _create_drops(self):
        """创建一串雨滴"""
        #创建一个雨滴再不断添加,直到没有空间添加雨滴为止
        #雨滴的间距为雨滴的宽度
        drop=Raindrop(self)
        drop_width,drop_height=drop.rect.size
        current_x,current_y=drop_width,drop_height
        while current_y<self.settings.screen_height-2*drop_height:#只留下最后两行
            while current_x<self.settings.screen_width-2*drop_width:
                self._create_drop(current_x,current_y)
                current_x+=2*drop_width

            current_x=drop_width
            current_y+=2*drop_height

    def _create_drop(self,x_postion,y_position):
        """创建一行雨滴并将其放在一行中"""
        new_drop=Raindrop(self)
        new_drop.y=y_position
        new_drop.rect.x=x_postion
        new_drop.rect.y=y_position
        self.raindrops.add(new_drop)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        #让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    rd_game=RaindropsGame()
    rd_game.run_game()

