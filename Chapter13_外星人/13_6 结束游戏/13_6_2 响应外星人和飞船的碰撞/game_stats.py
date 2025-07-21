class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self,ai_game):
        """跟踪游戏的统计信息"""
        self.settings=ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left=self.settings.ship_limit
        #玩家在一开始拥有的飞船数存储在settings类的ship_limit属性中
