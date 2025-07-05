import pygame

class Ship():
    def __init__(self,ai_game):
        '''初始化飞船并设置其初始位置'''
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('../main/images/ship.bmp')#返回表示飞船的的一个surface
        self.rect=self.image.get_rect()
        #📦 根据图像（Surface）生成一个矩形（Rect），用于定位和碰撞检测。

        #将每艘新飞船都放在屏幕底部中央
        self.rect.midbottom=self.screen_rect.midbottom

        #移动标志
        self.moving_right=False
        self.moving_left=False

    def update(self):
        '''根据移动标志调整飞船的位置'''
        if self.moving_right:
            self.rect.x+=1
        if self.moving_left:
            self.rect.x-=1
        #这里为了保持左右方向键同时处于优先位置，所以两个循环都用了if

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)#将图像绘制到rect指定的位置
        # blit() 是 Pygame 中的一个函数，用于将一个图像（Surface）绘制到另一个图像（Surface）上。
        # 这里是把飞船的图像绘制到屏幕上。