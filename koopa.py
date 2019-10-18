# Rey Vergara
# 10/17/19 Initial creation

import pygame
from pygame.sprite import Sprite

# Koopa settings
# self.koopa_width = 8 * self.image_scale
# self.koopa_height = 16 * self.image_scale
# self.koopa_speed = 1 * self.image_scale


class Koopa(Sprite):

    def __init__(self, screen, settings):
        super(Koopa, self).__init__()
        self.settings = settings
        self.screen = screen

        self.facing_right = False
        self.fall = False
        self.index = 0
        self.last_tick = pygame.time.get_ticks()

        self.current_image = pygame.transform.scale(pygame.image.load("images/koopa_2.png"),
                                                    (self.settings.koopa_width, self.settings.koopa_height))

        self.current_rect = self.current_image.get_rect()

        self.images = []
        self.images.extend([pygame.transform.scale(pygame.image.load("images/koopa_2.png"),
                                                   (self.settings.koopa_width, self.settings.koopa_height)),
                           pygame.transform.scale(pygame.image.load("images/koopa_1.png"),
                                                  (self.settings.koopa_width, self.settings.koopa_height))])

    def draw(self):
        self.screen.blit(self.current_image, self.current_rect)

    def update(self):
        self.iterate_index(len(self.images))
        self.current_image = self.images[self.index]

        if self.facing_right:
            self.current_rect.centerx += 1
        else:
            self.current_rect.centerx -= 1

    def iterate_index(self, max_):
        time = pygame.time.get_ticks() - self.last_tick
        if time > 100:
            self.index += 1
            self.last_tick = pygame.time.get_ticks()

        if self.index == max_:
            self.index = 0