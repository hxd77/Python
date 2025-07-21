class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230, 230, 230)

        #飞船设置
        self.ship_speed=5
        self.ship_limit=3

        #子弹设置
        self.bullet_speed=5
        self.bullet_width=30
        self.bullet_height=30
        self.bullet_color=(60, 60, 60)
        self.bullet_allowed=10

        #目标设置
        self.target_height=120
        self.target_width=15
        self.target_color=(180,60,10)
        self.target_speed=1.5

        #总体动态设置
        self.miss_limit=3