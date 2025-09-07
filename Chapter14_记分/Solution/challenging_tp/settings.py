class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230, 230, 230)

        #飞船设置
        self.ship_limit=3

        #子弹设置
        self.bullet_width=30
        self.bullet_height=30
        self.bullet_color=(60, 60, 60)
        self.bullet_allowed=10

        #目标设置
        self.target_height=120
        self.target_width=15
        self.target_color=(180,60,10)

        #总体动态设置
        self.miss_limit=300
        self.speedup_scale=2.1

        #难度设置,每次击中后都会提高难度
        self.levelsup_hits=10

        self.initialize_dynamic_settins()

    def initialize_dynamic_settins(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed=3.0
        self.bullet_speed=12.0
        self.target_speed=1.5

    def increase_speed(self):
        """提高速度设置的值"""
        self.ship_speed=self.ship_speed*self.speedup_scale
        self.bullet_speed=self.bullet_speed*self.speedup_scale
        self.target_speed=self.target_speed*self.speedup_scale

