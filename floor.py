# Jeffrey Lo
#
# 10/18/19 Initial creation - JL
import pygame
from pygame import image
from pygame.sprite import Sprite


class Floor(Sprite):
    def __init__(self, screen, settings, is_underground=False):
        super(Floor, self).__init__()
        self.screen = screen
        self.settings = settings

        if is_underground:
            self.current_image = pygame.transform.scale(
                image.load(settings.floor_ug_image),
                (self.settings.brick_width,
                 self.settings.brick_height)
            )
        else:
            self.current_image = pygame.transform.scale(
                image.load(settings.floor_image),
                (self.settings.brick_width,
                 self.settings.brick_height)
        )
        self.current_rect = self.current_image.get_rect()

    def draw(self):
        self.screen.blit(self.current_image, self.current_rect)
