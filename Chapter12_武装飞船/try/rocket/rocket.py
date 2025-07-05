import pygame

class Rocket:
    def __init__(self,r_game):
        #初始化火箭和设定初始位置
        self.screen=r_game.screen
        self.settings=r_game.settings
        self.screen_rect=r_game.screen.get_rect()

        #加载火箭图片和它的矩形
        self.image=pygame.image.load('images/rocket_small.png')
        self.rect=self.image.get_rect()

        #每一个火箭开始在屏幕中间
        self.rect.center=self.screen_rect.center

        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

        #移动标志
        self.moving_right,self.moving_left= False,False
        self.moving_up,self.moving_down= False,False

    def update(self):
        #根据移动标志调整火箭的位置
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.rocket_speed
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.x-=self.settings.rocket_speed
        if self.moving_up and self.rect.top>0:
            self.y-=self.settings.rocket_speed
        if self.moving_down and self.rect.bottom<=self.screen_rect.bottom:
            self.y+=self.settings.rocket_speed

        #更新rect对象的位置
        self.rect.x=self.x
        self.rect.y=self.y
    def blitme(self):
        '''画出火箭现在的位置'''
        self.screen.blit(self.image,self.rect)
