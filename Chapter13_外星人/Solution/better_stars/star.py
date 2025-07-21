import pygame
from pygame.sprite import Sprite
class Star(Sprite):
    def __init__(self,stars_game):
        super().__init__()
        self.settings=stars_game.settings
        self.screen=stars_game.screen
        self.image=pygame.image.load('images/star.png')
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

