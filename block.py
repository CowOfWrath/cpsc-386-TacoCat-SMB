# Jeffrey Lo
#
# 10/18/19 Initial creation - JL
#   Brick, CoinBrick, Brick Pieces
from pygame.sprite import Sprite
from pygame import image
from pygame import mixer

import pygame
from coin import Coin


class Block(Sprite):
    INVISIBLE = 'invisible'
    UNDERGROND = 'underground'
    COIN = 'coin'
    MYSTERY = 'mystery'

    def __init__(self, screen, settings, is_underground=False, is_invisible=False):
        super(Block, self).__init__()
        self.screen = screen
        self.settings = settings
        self.is_underground = is_underground
        self.last_tick = pygame.time.get_ticks()

        # Block States
        self.is_broken = False
        # TODO: add break block code

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

    def collision_check(self, sprite_object):
        pass

    def update(self):
        pass

    def animate_block_movement(self):
        # TODO animate block
        pass

    def animate_internal_object(self, sprite_object):
        # TODO animate internal object
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def iterate_index(self, max):
        time = pygame.time.get_ticks() - self.last_tick
        if time > 100:
            self.index += 1
            self.last_tick = pygame.time.get_ticks()
        if self.index == max:
            self.index = 0


class BrickRubblePiece(Sprite):
    def __init__(self, screen, settings, isLeft=True):
        super(BrickRubblePiece, self).__init__()
        self.screen = screen
        self.settings = settings
        self.f_index = 0
        self.image = None
        self.frames_list = []
        self.image_left = pygame.transform.scale(
            image.load(settings.brick_rubble_left),
            settings.brick_rubble_width,
            settings.brick_rubble_height
        )
        self.image_right = pygame.transform.scale(
            image.load(settings.brick_rubble_right),
            settings.brick_rubble_width,
            settings.brick_rubble_height
        )

        if isLeft:
            self.image = self.image_left
            self.frames_list[::2] = [self.image_left] * 4
            self.frames_list[1::2] = [self.image_right] * 4

        else:
            self.image = self.image_right
            self.frames_list[::2] = [self.image_left] * 4
            self.frames_list[1::2] = [self.image_right] * 4
        self.rect = self.image.get_rect()

    def update(self):
        self.iterate_index(len(self.frames_list))
        self.image = self.frames_list[self.f_index]
        # TODO: Animate Rubble Movement

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def iterate_index(self, max):
        time = pygame.time.get_ticks() - self.last_tick
        if time > 100:
            self.f_index += 1
            self.last_tick = pygame.time.get_ticks()
        if self.f_index == max:
            # self.f_index = 0
            self.kill()


class CoinBlock(Block):
    def __init__(self, screen, settings, is_underground=False, coins=0):
        super(CoinBlock, self).__init__(screen, settings, is_underground)
        self.num_coins_left = coins
        self.coins = []
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

    def init_coin_list(self):
        for i in range(self.num_coins_left):
            self.coins.append(Coin(self.screen, self.settings))

    def collision_check(self, sprite_object):
        if self.is_hittable:
            did_collide = self.rect.collidepoint(sprite_object.rect.midtop)
            if did_collide:
                # TODO - figure out if need to adjust collided object physics

                # Check if coins
                if self.num_coins_left > 0:
                    self.num_coins_left -= 1

                    # Animate Coin Trigger
                    # TODO call coin animation - Make sure coin animation plays points

                    # Play Coin Sound
                    self.sound.play()

                    # Set coinblock to empty if no coins
                    if self.num_coins_left <= 0:
                        self.set_empty()
        # else:
        #     # if collides, force mario back down
