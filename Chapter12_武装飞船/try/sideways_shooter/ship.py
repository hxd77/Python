import pygame
class Ship:
    def __init__(self,ss_game):
        """初始化火箭并设置其初始位置"""
        self.screen=ss_game.screen
        self.settings=ss_game.settings
        self.screen_rect=ss_game.screen.get_rect()
        self.image=pygame.image.load('images/rocket_small .png')
        self.rect=self.image.get_rect()

        #将每艘飞船放在屏幕左侧中间
        self.rect.midleft=self.screen_rect.midleft

        #在飞船的属性中存储一个浮点值
        self.y=float(self.rect.y)

        #设置两个移动标志
        self.moving_top=False
        self.moving_bottom=False

    def update(self):
        """根据移动标志来移动飞船"""
        if self.moving_top and self.rect.top>0:
            self.y-=self.settings.ship_speed
        elif self.moving_bottom and self.rect.bottom<self.screen_rect.bottom:
            self.y+=self.settings.ship_speed
        self.rect.y=self.y

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image,self.rect)
