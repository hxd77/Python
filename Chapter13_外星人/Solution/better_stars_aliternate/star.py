import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """管理一个单一星星的类"""
    def __init__(self,star_game):
        """初始化星星并设置位置"""
        super().__init__()
        self.screen=star_game.screen

        #加载星星的图片
        self.image=pygame.image.load('images/star.png')
        self.rect=self.image.get_rect()

        #每个星星的位置在屏幕的左边
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        
