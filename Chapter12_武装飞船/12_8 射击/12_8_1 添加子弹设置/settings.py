class Settings:
    '''存储《外星人入侵》的所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230, 230, 230)
        self.ship_speed=1.5

        #子弹设置
        self.bullet_speed=2.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60, 60, 60)
        #创建宽3要素、高15要素的深灰色子弹，子弹速度比飞船快

