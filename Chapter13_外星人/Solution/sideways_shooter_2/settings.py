class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230, 230, 230)
        self.ship_speed=5

        #子弹设置
        self.bullet_speed=5
        self.bullet_width=30
        self.bullet_height=30
        self.bullet_color=(60, 60, 60)
        self.bullet_allowed=10

        #外星人设置
        #alien_frequency控制生成一个新外星人概率，概率越高概率越大最大是1
        self.alien_frequency=0.008
        self.alien_speed=1.5
