# Jeffrey Lo
#
# 10/18/19 Initial creation - JL
from pygame.sprite import Sprite
from pygame import image
from pygame import mixer

import pygame


class Block(Sprite):
    def __init__(self, screen, settings, is_underground=False, is_invisible=False):
        super(Block, self).__init__()
        self.screen = screen
        self.settings = settings
        self.is_underground = is_underground

        # initial block image
        if is_underground:
            self.initial_image = pygame.transform.scale(
                image.load(settings.floor_ug_image),
                (self.settings.brick_width,
                 self.settings.brick_height)
            )
        else:
            self.initial_image = pygame.transform.scale(
                image.load(settings.floor_image),
                (self.settings.brick_width,
                 self.settings.brick_height)
                )
        if is_invisible:
            self.initial_image = self.initial_image.copy()
            self.initial_image.fill((255, 255, 255, 0), None, pygame.BLEND_RGBA_MULT)

        self.image = self.initial_image
        self.rect = self.image.get_rect()

    def collision_check(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)


class CoinBlock(Block):
    def __init__(self, screen, settings, is_underground=False, coins=0):
        super(CoinBlock, self).__init__(screen, settings, is_underground)
        self.num_coins_left = coins
        self.empty_image = pygame.transform.scale(
            image.load(settings.block_empty),
            (self.settings.block_width,
             self.settings.block_height)
        )
        self.sound = mixer.Sound(settings.coin_block_sound)

        self.is_hittable = True if coins > 0 else False

    def set_empty(self):
        self.is_hittable = False
        self.image = self.empty_image






