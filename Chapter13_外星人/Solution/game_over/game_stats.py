class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self,ss_game):
        """跟踪游戏的统计信息"""
        self.settings=ss_game.settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left=self.settings.ship_limit

