# Ryan Chen - 893219394
#
# 10/17/19 Initial creation
#   Added basic settings and states
#   Added image handling and placeholders

import pygame
from pygame.sprite import Sprite


class Coin(Sprite):
    def __init__(self, screen, settings):
        super(Coin, self).__init__()
        self.screen = screen
        self.settings = settings

        self.idle = True
        self.kill = False
        self.index = 0
        self.last_tick = pygame.time.get_ticks()

        self.current_image = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                    (self.settings.coin_width, self.settings.coin_height))

        self.current_rect = self.current_image.get_rect()

        self.images_idle = []
        self.images_idle.append(pygame.transform.scale(pygame.image.load("Images/coin_idle1.png"),
                                                       (self.settings.coin_width, self.settings.coin_height)))
        self.images_idle.append(pygame.transform.scale(pygame.image.load("Images/coin_idle2.png"),
                                                       (self.settings.coin_width, self.settings.coin_height)))
        self.images_idle.append(pygame.transform.scale(pygame.image.load("Images/coin_idle3.png"),
                                                       (self.settings.coin_width, self.settings.coin_height)))
        self.images_idle.append(pygame.transform.scale(pygame.image.load("Images/coin_idle4.png"),
                                                       (self.settings.coin_width, self.settings.coin_height)))

        self.images_move = []
        self.images_move.append(pygame.transform.scale(pygame.image.load("Images/coin_move1.png"),
                                                       (self.settings.coin_width, self.settings.coin_height)))
        self.images_move.append(pygame.transform.scale(pygame.image.load("Images/coin_move2.png"),
                                                       (self.settings.coin_width, self.settings.coin_height)))
        self.images_move.append(pygame.transform.scale(pygame.image.load("Images/coin_move3.png"),
                                                       (self.settings.coin_width, self.settings.coin_height)))

    def draw(self):
        self.screen.blit(self.current_image, self.current_rect)

    def update(self):
        if self.idle:
            self.iterate_index(len(self.images_idle))
            self.current_image = self.images_idle[self.index]
        else:
            self.iterate_index(len(self.images_move))
            self.current_image = self.images_move[self.index]

    def iterate_index(self, max):
        time = pygame.time.get_ticks() - self.last_tick
        if time > 100:
            self.index += 1
            self.last_tick = pygame.time.get_ticks()
        if self.index == max:
            self.index = 0
            if not self.idle:
                # Kill coin (move animation used for coins generated from mystery boxes and multi hit bricks)
                self.kill = True  # in a separate function remove the sprite from all groups using Sprite.kill()
