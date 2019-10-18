import pygame
from pygame import image
from pygame.sprite import Sprite

class Floor(Sprite):
    def __init__(self, screen, settings, is_underground=False):
        super(Floor, self).__init__()
        self.screen = screen
        self.settings = settings

        if is_underground:
            self.image = pygame.transform.scale(
                image.load(settings.brick_ug_image),
                (self.settings.brick_width,
                 self.settings.brick_height)
            )
        else:
            self.image = pygame.transform.scale(
                image.load(settings.brick_image),
                (self.settings.brick_width,
                 self.settings.brick_height)
        )
        self.rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, self.rect)
