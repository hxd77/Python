from random import randint

import pygame
from pygame.sprite import Sprite

class Target:
    """"表示单个目标的类"""
    def __init__(self,ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.screen_rect=self.screen.get_rect()

        self.settings = ss_game.settings
        self.color=self.settings.target_color

        # 创造矩形位置
        self.rect=pygame.Rect(0,0,self.settings.target_width,self.settings.target_height)
        #在(0,0)处创建一个宽target_width长为target_height的矩形

        self.center_target()

        self.direction=1
        #1表示下，-1表示上

    def update(self):
        #向左移动外星人
        self.y += self.settings.target_speed*self.direction

        if self.rect.top <0:
            #如果移动到超出屏幕上边，则往下移动
            self.rect.top=0
            self.direction=1
        elif self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom=self.screen_rect.bottom
            self.direction=-1

        self.rect.y=self.y

    def center_target(self):
        """目标在屏幕右中间"""
        self.rect.midright=self.screen_rect.midright

        self.y=float(self.rect.y)

    def draw_target(self):
        """在屏幕上绘制矩形"""
        pygame.draw.rect(self.screen,self.color,self.rect)