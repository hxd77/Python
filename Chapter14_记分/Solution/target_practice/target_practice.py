from settings import Settings
from ship import Ship
from bullet import Bullet
import pygame
import sys
from random import random
from target import Target
from game_stats import GameStats
from 外星人入侵.button import Button


class TargetPractice:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        self.stats=GameStats(self)
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.target=Target(self)

        #制作按钮
        self.play_button=Button(self,"Play")

        #游戏启动后处于不活动状态
        self.game_active=False

    def run_game(self):
        """开始游戏循环"""
        while True:
            #侦听键盘和鼠标事件
            self._check_events()
            if self.game_active:
                #每次循环时都重新绘制屏幕
                self.ship.update()
                self._update_bullets()
                self.target.update()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self,mouse_pos):
        """在玩家单击Play按钮时开始游戏"""
        button_clicked=self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _start_game(self):
        #重置游戏的统计信息
        self.stats.reset_stats()
        self.game_active=True

        #清空子弹
        self.bullets.empty()

        #飞船和目标放中间
        self.ship.center_ship()
        self.target.center_target()

        #隐藏鼠标光标
        pygame.mouse.set_visible(False)

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
                self._increment_misses()

        self._check_bullet_target_collisions()

    def _increment_misses(self):
        """增加未命中的次数，并且检查到3次没"""
        self.stats.num_misses+=1
        if self.stats.num_misses==self.settings.miss_limit:
            self.game_active=False
            pygame.mouse.set_visible(True)

    def _check_bullet_target_collisions(self):
        """检查子弹和外星人之间的碰撞"""
        collisions = pygame.sprite.spritecollide(self.target, self.bullets, True)


    def _update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()

        self.target.draw_target()

        #如果处于非活动状态，就绘制Play按钮
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()





if __name__=='__main__':
    ss_game=TargetPractice()
    ss_game.run_game()
