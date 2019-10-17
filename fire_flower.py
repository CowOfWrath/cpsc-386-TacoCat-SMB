# Ryan Chen - 893219394
#
# 10/17/19 Initial creation - RC
#   Added basic settings and states
#   Added image handling and placeholders

import pygame
from pygame.sprite import Sprite


class Fire_Flower(Sprite):
    def __init__(self, screen, settings):
        super(Fire_Flower, self).__init__()
        self.screen = screen
        self.settings = settings

        self.index = 0
        self.last_tick = pygame.time.get_ticks()

        self.current_image = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                    (self.settings.fire_flower_width, self.settings.fire_flower_height))

        self.current_rect = self.current_image.get_rect()

        self.images = []
        self.images.append(pygame.transform.scale(pygame.image.load("Images/fire_flower_1.png"),
                                                  (self.settings.fire_flower_width, self.settings.fire_flower_height)))
        self.images.append(pygame.transform.scale(pygame.image.load("Images/fire_flower_2.png"),
                                                  (self.settings.fire_flower_width, self.settings.fire_flower_height)))
        self.images.append(pygame.transform.scale(pygame.image.load("Images/fire_flower_3.png"),
                                                  (self.settings.fire_flower_width, self.settings.fire_flower_height)))
        self.images.append(pygame.transform.scale(pygame.image.load("Images/fire_flower_4.png"),
                                                  (self.settings.fire_flower_width, self.settings.fire_flower_height)))

    def draw(self):
        self.screen.blit(self.current_image, self.current_rect)

    def update(self):
        self.iterate_index(len(self.images))
        self.current_image = self.images[self.index]

    def iterate_index(self, max):
        time = pygame.time.get_ticks() - self.last_tick
        if time > 100:
            self.index += 1
            self.last_tick = pygame.time.get_ticks()
        if self.index == max:
            self.index = 0
