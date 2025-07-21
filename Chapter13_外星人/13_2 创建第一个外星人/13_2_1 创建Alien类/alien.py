import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self,ai_game):
        """初始化外星人并设置其初始位置"""
        """__init__() 方法接受创建 Sprite 实例所需的信息"""
        super().__init__()
        self.screen=ai_game.screen

        #加载外星人图像并设置其rect属性
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        #每个外星人最初都在屏幕的左上角附近
        self.rect.x=self.screen_rect.width
        self.rect.y=self.screen_rect.height

        #存储外星人的精确水平位置
        self.x=float(self.rect.x)

