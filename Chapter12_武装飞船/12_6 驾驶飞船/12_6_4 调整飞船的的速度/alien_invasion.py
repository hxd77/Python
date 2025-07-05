import sys
import pygame
from aioquic.h3.connection import Setting
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    #创建一艘飞船
    ship=Ship(ai_settings,screen)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
        '''
        pygame.display.flip() 是 Pygame 中的一个函数，用来更新整个窗口的内容，让你在屏幕上“看到”你画的东西。
        🎮 通俗解释
        在 Pygame 中，所有图像操作（绘图、贴图、文字等）都是先画在屏幕的内存缓冲区（Surface）里。
        这就像在草稿纸上画画，画好了才一次性展示给用户看。
    
        👉 pygame.display.flip() 就是把这张“草稿纸” 翻到屏幕上显示 —— 也就是 “刷新画面”。
    '''
run_game()