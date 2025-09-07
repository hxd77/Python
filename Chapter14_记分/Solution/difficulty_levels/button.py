import pygame.font

class  Button:
    """为游戏创建按钮的类"""
    def __init__(self, ai_game,msg):
        """初始化按钮的属性"""
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()

        #设置按钮的尺寸和其他属性
        self.width,self.height=200,50
        self.button_color=(0,135,0)  #让按钮的rect对象为绿色
        self.text_color=(255,255,255)  #text_color为白色
        self.font=pygame.font.SysFont(None,48) #None使用默认字体，48制定了文本的字号

        #创建按钮的rect对象，并使其居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        #按钮的标签只需创建一次
        self._preg_msg(msg)

    def _preg_msg(self,msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        """font.render将存储在msg中的文本转换为图像，True表示开启反锯齿功能"""
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
        """让文本图像在按钮上居中"""

    def _update_msg_position(self):
        """如果按钮被移动了，那么文字也会移动"""
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""
        self.screen.fill(self.button_color,self.rect)   #绘制按钮的矩形
        """表示在 self.screen 这个 Surface 上，用 self.button_color 填充 self.rect 所表示的区域，
        相当于在该区域画一个“纯色矩形”。"""
        self.screen.blit(self.msg_image,self.msg_image_rect)    #blit传递一幅图像以及图像相关的rect

