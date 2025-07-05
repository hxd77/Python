import sys
import pygame

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    self.clock=pygame.time.Clock()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    #设置背景色
    bg_color=(230,230,230)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        #每次循环时都重绘屏幕
        screen.fill(bg_color)
        #让最近绘制的屏幕可见
        pygame.display.flip()
        self.clock.tick(60)
        '''
        pygame.display.flip() 是 Pygame 中的一个函数，用来更新整个窗口的内容，让你在屏幕上“看到”你画的东西。
        🎮 通俗解释
        在 Pygame 中，所有图像操作（绘图、贴图、文字等）都是先画在屏幕的内存缓冲区（Surface）里。
        这就像在草稿纸上画画，画好了才一次性展示给用户看。
    
        👉 pygame.display.flip() 就是把这张“草稿纸” 翻到屏幕上显示 —— 也就是 “刷新画面”。
    '''
run_game()