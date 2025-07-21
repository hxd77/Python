from settings import Settings
from ship import Ship
from bullet import Bullet
import pygame
import sys
class SidewaysShooters:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()

    def run_game(self):
        """开始游戏循环"""
        while True:
            #侦听键盘和鼠标事件
            self._check_events()
            #每次循环时都重新绘制屏幕
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

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
        """按下按键"""
        if event.key==pygame.K_UP:
            self.ship.moving_top=True
        elif event.key==pygame.K_DOWN:
            self.ship.moving_bottom=True
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
        elif event.key==pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key==pygame.K_UP:
            self.ship.moving_top=False
        elif event.key==pygame.K_DOWN:
            self.ship.moving_bottom=False

    def _fire_bullet(self):
        """发射子弹"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet= Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹并删除消失的子弹"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left>=self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        pygame.display.flip()

if __name__=='__main__':
    ss_game=SidewaysShooters()
    ss_game.run_game()
