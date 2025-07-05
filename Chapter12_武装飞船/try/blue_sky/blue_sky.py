import sys
import pygame

from settings import Settings

class BlueSkyGame():
    '''A class to manage the game assets and behavior.'''
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()#Pygame 中用于创建一个时钟对象的代码。这个时钟对象可以用来控制游戏循环的帧率（FPS，Frames Per Second）。
        self.settings=Settings()

        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Blue Sky Game")

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()

            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            #Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)#设置游戏循环的帧率为60帧每秒

if __name__ =='__main__':
    #Make a game instance, and run the game.
    blue_sky=BlueSkyGame()
    blue_sky.run_game()
