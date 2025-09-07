import pygame.font
from pygame.sprite import Group

from ship import Ship

class ScoreBoard:
    """显示得分的类"""
    def __init__(self, ai_game):
        """初始化显示得分涉及的属性"""
        self.ai_game=ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings=ai_game.settings
        self.stats=ai_game.stats

        #显示得分信息时使用的字体
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None, 48)

        self.prep_images()

    def prep_images(self):
        # 准备包含最高分和当前得分的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        """将得分渲染为图像"""
        rounded_score=round(self.stats.score,-1)#x：要四舍五入的数字 n：保留的小数位数（正数表示保留几位小数，负数表示四舍五入到十位、百位等）
        score_str=f"{rounded_score:,}"#转换成字符串加上数字格式控制，插入,显示如1000,000,000
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)#传递屏幕背景板颜色和文本颜色

        #在屏幕右上角显示得分
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right - 20
        self.score_rect.top=20
        """为了确保得分始终锚定在屏幕右上角，当位数增加导致数更宽时，它会向左延伸。创建一个名为score_rect的rect，让其右边缘与屏幕右边缘相距20像素，并让其上边缘与屏幕上边缘也相聚20像素"""

    def prep_high_score(self):
        """将最高分渲染为图像"""
        high_score=round(self.stats.high_score,-1)
        high_socre_str=f"{high_score:,}"
        self.high_score_image=self.font.render(high_socre_str,True,self.text_color,self.settings.bg_color)

        #将最高分放在屏幕顶部的中央
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top

    def prep_level(self):
        """将等级渲染为图像"""
        level_str=str(self.stats.level)
        self.level_image=self.font.render(level_str,True,self.text_color,self.settings.bg_color)

        #将等级放在得分下面
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+10

    def prep_ship(self):
        """显示还剩下多少艘飞船"""
        self.ships=Group()#一个空编组，用来存储飞船实例
        for ship_number in range(self.stats.ships_left):#根据还剩多少艘飞船以此来遍历循环
            ship=Ship(self.ai_game)#创建新飞船并设置x坐标
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上绘制得分、等级和余下的飞船数"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """检查是否诞生了新的最高分"""
        if self.stats.score>self.stats.high_score:
            self.stats.high_score=self.stats.score
            self.prep_high_score()


