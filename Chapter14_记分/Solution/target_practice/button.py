import pygame.font

class Button:
    def __init__(self,ss_game,msg):
        """初始化按键设置"""
        self.screen=ss_game.screen
        self.screen_rect=ss_game.screen.get_rect()

        #设置按钮的特征
        self.width,self.height=200,50
        self.button_color=(100,5,5)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        #创建按钮的rect对象，并使其居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        #按钮标签只需创建一次
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """将msg渲染成图像，并使其在按钮上居中"""
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        """绘制一个按钮再绘制文本"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)