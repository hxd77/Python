from pygame.sprite import Sprite
import pygame
class Bullet(Sprite):
    def __init__(self, ss_game):
        super().__init__()
        self.screen=ss_game.screen
        self.settings=ss_game.settings
        self.color=self.settings.bullet_color

        #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midleft=ss_game.ship.rect.midright

        #存储用浮点数表示的子弹位置
        self.x=float(self.rect.x)

    def update(self):
        """向右更新子弹"""
        #更新子弹的的准确位置
        self.x+=self.settings.bullet_speed
        #更新表示子弹的rect位置
        self.rect.x=self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)

