import sys
import pygame
from settings import Settings
from rocket import Rocket

class RocketGame:
    def __init__(self):
        #初始化游戏并创建游戏资源
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()

        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Rocket Game")
        self.rocket=Rocket(self)

    def run_game(self):
        '''开始加载主要游戏'''
        while True:
            self.check_events()
            self.rocket.update()
            self.update_screen()
            self.clock.tick(60)#游戏的最大帧率保持在 60 帧每秒（FPS）。防止游戏运行太快

    def check_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self,event):
        '''响应按键按下'''
        if event.key==pygame.K_RIGHT:
            self.rocket.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.rocket.moving_left=True
        elif event.key==pygame.K_UP:
            self.rocket.moving_up=True
        elif event.key==pygame.K_DOWN:
            self.rocket.moving_down=True

    def check_keyup_events(self,event):
        '''响应按键松开'''
        if event.key==pygame.K_RIGHT:
            self.rocket.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.rocket.moving_left=False
        elif event.key==pygame.K_UP:
            self.rocket.moving_up=False
        elif event.key==pygame.K_DOWN:
            self.rocket.moving_down=False

    def  update_screen(self):
        '''更新屏幕上的图像，并切换到新屏幕'''
        #每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()
        '''
        pygame.display.flip() 是 Pygame 中的一个函数，用来更新整个窗口的内容，让你在屏幕上“看到”你画的东西。
        🎮 通俗解释
        在 Pygame 中，所有图像操作（绘图、贴图、文字等）都是先画在屏幕的内存缓冲区（Surface）里。
        这就像在草稿纸上画画，画好了才一次性展示给用户看。
    
        👉 pygame.display.flip() 就是把这张“草稿纸” 翻到屏幕上显示 —— 也就是 “刷新画面”。'''

if __name__=='__main__':
    #创建一个游戏实例并运行游戏
    rg=RocketGame()
    rg.run_game()