import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏循环"""
        while True:
            # 侦听键盘和鼠标事件
            self._check_events()
            # 每次循环时都重新绘制屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()  # 绘制飞船

            # 让最近绘制的屏幕可见
            pygame.display.flip()
            self.clock.tick(60)

    # 辅助方法一般只在类中调用，不会在类外调用，在Python中，辅助方法的名称以单下划线打头
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
