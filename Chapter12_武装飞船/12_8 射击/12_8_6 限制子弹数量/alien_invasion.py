import sys
from traceback import print_tb

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

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
        """"""
        self.bullets=pygame.sprite.Group()
        """pygame.sprite.Group 是 Pygame 提供的一个类，用于存储和管理多个精灵（Sprite 对象）。
        它可以方便地对一组精灵进行操作，例如更新位置、检测碰撞或绘制到屏幕上。  在这里，self.bullets 是一个精灵组，
        用来存储游戏中所有的子弹对象。这样可以轻松地对所有子弹进行统一管理，例如更新它们的位置或绘制它们到屏幕上。"""
    def run_game(self):
        """开始游戏循环"""
        while True:
            # 侦听键盘和鼠标事件
            self._check_events()
            # 每次循环时都重新绘制屏幕
            self.ship.update()
            self.bullets.update()
            #对编组调用update时，编组会自动对其中的每个精灵调用update()

            #删除已消失的子弹
            for bullet in self.bullets.copy():
                '''的作用是遍历 self.bullets 编组中的所有子弹对象。这里使用了 .copy() 方法，
                是为了在遍历时创建 self.bullets 的副本，避免在循环中直接修改原始编组（例如删除子弹）导致遍历出错或抛出异常。 '''
                if bullet.rect.bottom < 0:#如果子弹的底部坐标y小于0，说明子弹已经飞出屏幕
                    self.bullets.remove(bullet)
                #print(len(self.bullets))
            self._update_screen()
            self.clock.tick(60)

    # 辅助方法一般只在类中调用，不会在类外调用，在Python中，辅助方法的名称以单下划线打头
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        """响应按键按下事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            #按下空格开火
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets，编组像一个列表"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():#这里加sprites()是为了将编组转化为列表，返回一个列表，其中包含所有子弹
            bullet.draw_bullet()
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
