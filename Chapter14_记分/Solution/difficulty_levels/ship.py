import pygame

class Ship:
    def __init__(self,ai_game):
        '''初始化飞船并设置其初始位置'''
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()
        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')#返回表示飞船的的一个surface
        self.rect=self.image.get_rect()
        #📦 根据图像（Surface）生成一个矩形（Rect），用于定位和碰撞检测。

        #将每艘新飞船都放在屏幕底部中央
        self.rect.midbottom=self.screen_rect.midbottom

        #在飞船的属性x中存储一个浮点数
        self.x=float(self.rect.x)

        #移动标志(飞船一开始不移动)
        self.moving_right=False
        self.moving_left=False

    def center_ship(self):
        """将飞船放在屏幕底部的额中央"""
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)

    def update(self):
        '''根据移动标志调整飞船的位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x-=self.settings.ship_speed
        #这里为了保持左右方向键同时处于优先位置，所以两个循环都用了if

        #更新飞船的rect对象，而不是直接更新self.rect.x
        self.rect.x=self.x

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)#将图像绘制到rect指定的位置
        # blit() 是 Pygame 中的一个函数，用于将一个图像（Surface）绘制到另一个图像（Surface）上。
        # 这里是把飞船的图像绘制到屏幕上。