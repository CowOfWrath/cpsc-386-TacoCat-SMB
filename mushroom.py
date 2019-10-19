# Rey Vergara
# 10/18/19 - Created
# Has basic movement
# No image array since
# Mushroom is static when moving

import pygame
from pygame.sprite import Sprite


class Mushroom(Sprite):
    def __init__(self, screen, settings):
        super(Mushroom, self).__init__()
        self.screen = screen
        self.settings = settings
        self.going_left = False

        self.image = pygame.transform.scale(pygame.image.load("images/mushroom"),
                                            self.settings.mushroom_width, self.settings.mushroom_height)
        self.mushroom_rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, self.mushroom_rect)

    def update(self):
        if self.going_left:
            self.mushroom_rect -= self.settings.mushroom_speed
        else:
            self.mushroom_rect += self.settings.mushroom_speed
