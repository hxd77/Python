import pygame.font

class ScoreBoard:
    """显示得分的类"""
    def __init__(self, ai_game):
        """初始化显示得分涉及的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings=ai_game.settings
        self.stats=ai_game.stats

        #显示得分信息时使用的字体
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None, 48)

        #准备初始得分图像
        self.prep_score()

    def prep_score(self):
        """将得分渲染为图像"""
        score_str=str(self.stats.score)#转换成字符串
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)#传递屏幕背景板颜色和文本颜色

        #在屏幕右上角显示得分
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right - 20
        self.score_rect.top=20
        """为了确保得分始终锚定在屏幕右上角，当位数增加导致数更宽时，它会向左延伸。创建一个名为score_rect的rect，让其右边缘与屏幕右边缘相距20像素，并让其上边缘与屏幕上边缘也相聚20像素"""

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image,self.score_rect)



