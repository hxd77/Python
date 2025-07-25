import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船所发射子弹的类"""
    def __init__(self,ai_game):
        """在飞船的当前位置创建一个子弹对象"""
        super().__init__()#super()是父类
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color=self.settings.bullet_color

        #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midbottom=ai_game.ship.rect.midtop

        #存储用浮点数表示的子弹位置
        self.y=float(self.rect.y)

    def update(self):
        """向上更新子弹"""
        #更新子弹的的准确位置
        self.y-=self.settings.bullet_speed
        #更新表示子弹的rect位置
        self.rect.y=self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)