import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from time import sleep #导入sleep函数，以便飞船被外星人撞到后让游戏暂停一会

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)

        #创建飞船实例
        self.ship = Ship(self)
        """"""
        self.bullets=pygame.sprite.Group()
        """pygame.sprite.Group 是 Pygame 提供的一个类，用于存储和管理多个精灵（Sprite 对象）。
        它可以方便地对一组精灵进行操作，例如更新位置、检测碰撞或绘制到屏幕上。  在这里，self.bullets 是一个精灵组，
        用来存储游戏中所有的子弹对象。这样可以轻松地对所有子弹进行统一管理，例如更新它们的位置或绘制它们到屏幕上。"""
        self.aliens=pygame.sprite.Group()
        self._create_fleet()

        #游戏启动后处于活动状态
        self.game_active=True

    def run_game(self):
        """开始游戏循环"""
        while True:
            # 侦听键盘和鼠标事件
            self._check_events()

            if self.game_active:
                # 每次循环时都重新绘制屏幕
                self.ship.update()
                #对编组调用update时，编组会自动对其中的每个精灵调用update()
                self._update_bullet()
                self._update_aliens() #用于更新子弹后外星人的位置

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

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets，编组像一个列表"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    #为了确保AlienInvasion类的整洁,新创建一个_update_bullets()的方法
    def _update_bullet(self):
        """更新子弹的位置并删除已消息的子弹"""
        #更新子弹的位置
        self.bullets.update()

        #删除已消失的子弹
        for bullet in self.bullets.copy():
            """使用for循环遍历列表时，Python要求该列表的长度在整个循环中保持不变
            这意味着不能从for循环遍历的列表或编组中删除元素，因此必须遍历编组的副本copy"""
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)#移除某一颗子弹
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人之间的碰撞"""
        #检查是否有子弹击中了外星人
        #如果是，就删除相应的子弹和外星人
        collisions=pygame.sprite.groupcollide(self.bullets, self.aliens, True,True)
        """将self.bulltets和self.aliens编组中的元素的rect进行碰撞检测,看是否重叠，如果重叠groupcollide()就在返回的字典中
        添加一个键值对，键表示特定的子弹，值表示外星人，两个True表示子弹和外星人碰撞后都会消失"""

        if not self.aliens: #如果aliens为空
            #删除现有的子弹并创建一个新的外星舰队
            self.bullets.empty() #清空子弹编组
            self._create_fleet()

    """当有外星人撞到飞船时，将余下的飞船数减1，创建一个新的外星舰队，并将飞船重新放在屏幕底部的中央。
    另外，让游戏暂停一会，让玩家意识到发生了碰撞，并在创建新的外星舰队重整旗鼓"""

    def _create_fleet(self):
        """创建一个外星舰队"""
        # 创建一个外星人，再不断添加，直到没有空间添加外星人为止
        # 外星人的间距为外星人的宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < self.settings.screen_height - 3 * alien_height:  # 只留下底部三行
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # 添加一行外星人后，重置x值并递增y值
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """创建一行外星人并将其放在当前行中"""
        new_alien = Alien(self)
        new_alien.x = x_position  # 这句话不能删掉，
        """如果你没有 self.x = x_position，那么 self.x 这个属性在 Alien 类里可能会被初始化为默认值（比如0），
这样每个外星人的 self.x 都是0，update 的时候全部都从0开始移动，导致所有外星人都重叠在一列上，看起来就像只有一列/一行。"""
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _ship_hit(self):
        """响应飞船和外星人的碰撞"""
        if self.stats.ships_left>0:
            #将ships_left减1
            self.stats.ships_left -= 1

            #清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()

            #创建一个新的外星舰队，并将飞船放在屏幕底部的中央
            self._create_fleet()
            self.ship.center_ship()

            #暂停
            sleep(0.5)
        else:
            self.game_active=False

    def _update_aliens(self):
        """检测是否有外星人位于屏幕边缘，更新外星舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()  # 让组里的所有外星人都执行它们自己的 update() 方法

        # 检查是否有外形人撞到飞船
        if pygame.sprite.spritecollide(self.ship, self.aliens, dokill=False):
            self._ship_hit()
        """接受两个实参，一个精灵和一个编组，检查编组是否有成员与精灵发生了碰撞，并在找到与精灵发生碰撞的成员后停止遍历编组
        这里，遍历aliens编组，返回找到的第一个与飞船发生碰撞的外星人
        dokill=False：是否在检测到碰撞后自动把 aliens 中的碰撞项删掉（一般不删就设为 False）"""

        # 检查是否有外星人到达了屏幕边缘
        self._check_aliens_bottom()
    def _check_fleet_edges(self):
        """在有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整个外星舰队向下移动，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕的下边缘"""
        for alien in self.aliens.sprites():#返回编组元素
            if alien.rect.bottom>=self.settings.screen_height:
                #像飞船被撞到一样处理
                self._ship_hit()
                break

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets:  # 这里加sprites()是为了将编组转化为列表，返回一个列表，其中包含所有子弹
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        """self.aliens 是一个 pygame.sprite.Group 对象，包含所有外星人精灵。
        .draw(self.screen) 是 pygame.sprite.Group 提供的方法，它会自动遍历编组中的所有精灵，
        并调用每个精灵的 image 和 rect 属性，将它们绘制到指定的 screen 上
        draw()接受一个参数，这个参数制定了要将编组上的元素绘制到哪个surface上"""
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
