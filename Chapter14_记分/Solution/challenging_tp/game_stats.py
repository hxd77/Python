class GameStats:
    """跟踪游戏状态的类"""

    def __init__(self,ss_game):
        """初始化状态"""
        self.settings=ss_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left=self.settings.ship_limit
        self.num_misses=0
        self.num_hits=0

