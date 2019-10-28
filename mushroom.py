# Rey Vergara
# 10/18/19 - Created
#   Has basic movement
#   No image array since
#       Mushroom is static when moving
# Jeffrey Lo
# 10/18/19
#   Modified to support both 1-UP and regular mushroom

import pygame
from pygame.sprite import Sprite


class Mushroom(Sprite):
    def __init__(self, screen, settings, is_one_up = False):
        super(Mushroom, self).__init__()
        self.screen = screen
        self.settings = settings
        self.going_left = False
        self.is_one_up = is_one_up

        if self.is_one_up:
            self.image = pygame.transform.scale(pygame.image.load(settings.oneup_img),
                                                self.settings.mushroom_width, self.settings.mushroom_height)
        else:
            self.image = pygame.transform.scale(pygame.image.load(settings.mushroom_img),
                                            self.settings.mushroom_width, self.settings.mushroom_height)
        self.mushroom_rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, self.mushroom_rect)

    def update(self):
        # gravity
        # self.rect.centery += self.settings.gravity

        if self.going_left:
            self.mushroom_rect -= self.settings.mushroom_speed
        else:
            self.mushroom_rect += self.settings.mushroom_speed
