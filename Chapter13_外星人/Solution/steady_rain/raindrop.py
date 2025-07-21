import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self,rd_game):
        """初始化雨滴并设置其初始位置"""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        #加载雨滴图像并设置其rect属性
        self.image=pygame.image.load('../steady_rain/images/raindrop.png')
        self.rect=self.image.get_rect()

        #每个雨滴一开始都在屏幕的左上角
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #存储雨滴的准确位置
        self.y=float(self.rect.y)

    def check_disappered(self):
        """检查雨滴是否消失在屏幕底部"""
        if self.rect.top>self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        """向下移动雨滴"""
        self.y+=self.settings.raindrop_speed
        self.rect.y=self.y