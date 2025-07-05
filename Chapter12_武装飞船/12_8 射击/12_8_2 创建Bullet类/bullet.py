import pygame
from pygame.sprite import Sprite
"""from pygame.sprite import Sprite 是用于导入 pygame 中的 Sprite 类。  Sprite 是 pygame 提供的一个基类，用于管理游戏中的对象（如角色、子弹等）。它可以帮助你组织和管理多个游戏对象，
尤其是在使用 pygame.sprite.Group 时，可以方便地对一组精灵进行操作（如更新位置或绘制到屏幕上）。  在你的代码中，导入 Sprite 可能是为了创建一个继承自 Sprite 的类，用于定义游戏中的某种对象（例如子弹或角色）"""

class Bullet(Sprite):
    """一个对飞船发射子弹进行管理的类"""

    def __init__(self,ai_game):
        """在飞船所处的位置创建一个子弹对象"""
        super.__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        """参数 (0, 0): 表示矩形的初始位置，左上角的坐标为 (0, 0)。
self.settings.bullet_width 和 self.settings.bullet_height: 分别定义矩形的宽度和高度，这些值来自 Settings 类中的子弹设置。"""
        self.rect.midtop=ai_game.ship.rect.midtop
        """self.rect.midtop = ai_game.ship.rect.midtop 的作用是将子弹的矩形 (self.rect) 的顶部中心位置设置为飞船矩形 (ai_game.ship.rect) 的顶部中心位置。"""

        #存储用浮点数表示的子弹位置
        self.y=float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        #更新子弹的准确位置
        self.y-=self.settings.bullet_speed
        #更新表示子弹的rect的位置
        self.rect.y =self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        """选中的代码行 pygame.draw.rect(self.screen, self.color, self.rect) 的作用是使用 Pygame 的 draw.rect 方法在屏幕上绘制一个矩形。  具体含义如下：  
self.screen: 表示绘制矩形的目标 Surface（屏幕）。
self.color: 矩形的颜色，通常是一个 RGB 元组，例如 (255, 0, 0) 表示红色。
self.rect: 矩形的位置和大小，由 Pygame 的 Rect 对象定义。
这行代码会根据 self.rect 的位置和尺寸，在 self.screen 上绘制一个颜色为 self.color 的矩形"""
        #有图像才能有用pygame.screen.blit()方法