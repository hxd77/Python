from random import randint

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """"表示单个外星人的类"""
    def __init__(self,ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # 加载外星人图像并设置其 rect 属性
        self.image=pygame.image.load('images/alien_ship.png')
        self.rect=self.image.get_rect()

        #每个外星人在右侧的随机位置
        self.rect.right=self.screen.get_rect().right
        #我们将外星人放置在屏幕的最下方，其高度是屏幕的高度减去外星人的高度。
        alien_top_max=self.settings.screen_height-self.rect.height
        self.rect.top=randint(0,alien_top_max)

        # 存储外星人的精确水平位置
        self.x=float(self.rect.x)

    def update(self):
        #向左移动外星人
        self.x -= self.settings.alien_speed
        self.rect.x=self.x

