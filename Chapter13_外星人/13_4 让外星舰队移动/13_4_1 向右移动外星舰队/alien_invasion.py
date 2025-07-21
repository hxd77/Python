import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.aliens=pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """开始游戏循环"""
        while True:
            # 侦听键盘和鼠标事件
            self._check_events()
            # 每次循环时都重新绘制屏幕
            self.ship.update()
            #对编组调用update时，编组会自动对其中的每个精灵调用update()
            self._update_bullet()
            #更新完子弹位置后更新外星人位置，因为要检查有没有子弹击中外星人
            self._update_alien()
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

    #为了确保AlienInvasion类的整洁,新创建一个_update_bullets()的方法
    def _update_bullet(self):
        """更新子弹的位置并删除已消息的子弹"""
        #更新子弹的位置
        self.bullets.update()

        #删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
    def _update_alien(self):
        """更新外星舰队中所有外星人的位置"""

    def _create_fleet(self):
        """创建一个外星舰队"""
        #创建一个外星人，再不断添加，直到没有空间添加外星人为止
        #外星人的间距为外星人的宽度
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        current_x,current_y=alien_width,alien_height
        while current_y<self.settings.screen_height-3*alien_height:#只留下底部三行
            while current_x<(self.settings.screen_width-2*alien_width):
                self._create_alien(current_x,current_y)
                current_x+=2*alien_width

            #添加一行外星人后，重置x值并递增y值
            current_x=alien_width
            current_y+=2*alien_height

    def _create_alien(self,x_position,y_position):
        """创建一行外星人并将其放在当前行中"""
        new_alien=Alien(self)
        #new_alien.x=x_position
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets:#这里加sprites()是为了将编组转化为列表，返回一个列表，其中包含所有子弹
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
