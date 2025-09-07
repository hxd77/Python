import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self,ai_game):
        """初始化外星人并设置其初始位置"""
        """__init__() 方法接受创建 Sprite 实例所需的信息"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings

        #加载外星人图像并设置其rect属性
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        #每个外星人最初都在屏幕的左上角附近
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        """self.rect.width 是外星人图像矩形的宽度。
        self.rect.x 是外星人矩形的水平位置（左边缘的 x 坐标）。
        这行代码将外星人的水平位置设置为其宽度，确保外星人最初出现在屏幕左上角附近，并且距离屏幕左边缘的距离等于其自身宽度"""

        #存储外星人的精确水平位置
        self.x=float(self.rect.x)

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect=self.screen.get_rect()
        return (self.rect.right>=screen_rect.right) or (self.rect.left<=0)
        #查看是否超出右边缘或左边缘

    def update(self):
        """向左或向右移动外星人"""
        self.x+=self.settings.alien_speed*self.settings.fleet_direction
        self.rect.x=self.x


