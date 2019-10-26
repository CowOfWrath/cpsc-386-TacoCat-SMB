# Jeffrey Lo
#
# 10/18/19 Initial creation - JL
#   Brick, CoinBrick, Brick Pieces, Mystery block
from pygame.sprite import Sprite
from pygame import image
from pygame import mixer

import pygame
from coin import Coin
from fire_flower import Fire_Flower
from mushroom import Mushroom
from star import Star


class Block(Sprite):
    INVISIBLE = 'invisible'
    UNDERGROUND = 'underground'
    COIN = 'coin'
    MYSTERY = 'mystery'

    def __init__(self, screen, settings, is_underground=False):
        super(Block, self).__init__()
        self.screen = screen
        self.settings = settings
        self.is_underground = is_underground
        self.last_tick = pygame.time.get_ticks()
        self.index = 0

        # Block States
        self.is_hittable = True
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

        self.image = self.initial_image
        self.rect = self.image.get_rect()

    def collision_check(self, sprite_object):
        # TODO: if hittable, break block
        pass

    def update(self):
        pass

    def animate_block_movement(self):
        # TODO animate block
        pass

    def animate_internal_object(self, sprite_object):
        # TODO animate internal object to move to top of block
        if sprite_object:
            print('TODO - get sprite_object rect and move block')
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def iterate_index(self, max_index):
        time = pygame.time.get_ticks() - self.last_tick
        if time > 100:
            self.index += 1
            self.last_tick = pygame.time.get_ticks()
        if self.index == max_index:
            self.index = 0


class BrickRubblePiece(Sprite):
    def __init__(self, screen, settings, is_left=True):
        super(BrickRubblePiece, self).__init__()
        self.screen = screen
        self.settings = settings
        self.f_index = 0
        self.image = None
        self.last_tick = pygame.time.get_ticks()
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

        if is_left:
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

    def iterate_index(self, max_index):
        time = pygame.time.get_ticks() - self.last_tick
        if time > self.settings.brick_rubble_image_TBF:
            self.f_index += 1
            self.last_tick = pygame.time.get_ticks()
        if self.f_index == max_index:
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
            # TODO: JL Note - may need to check corner top collisions
            did_collide = self.rect.collidepoint(sprite_object.rect.midtop)
            if did_collide:
                # TODO - figure out if need to adjust collided object physics

                # Check if coins
                if self.num_coins_left > 0:
                    self.num_coins_left -= 1

                    # Animate Coin Trigger
                    # TODO call coin animation - Make sure coin animation plays points

                    # Play Coin Sounds
                    self.sound.play()

                    # Set coinblock to empty if no coins
                    if self.num_coins_left <= 0:
                        self.set_empty()
        # else:
        #     # if collides with bottom and empty, force mario back down


class MysteryBlock(Block):

    def __init__(self, screen, settings, is_underground=False, stored_item='', is_invisible=False):
        super(MysteryBlock, self).__init__(screen, settings, is_underground)
        self.empty_image = pygame.transform.scale(
            image.load(settings.block_empty),
            (self.settings.block_width,
             self.settings.block_height)
        )
        self.stored_item = stored_item
        self.images_idle = []
        for i in range(len(settings.mystery_block_images)):
            self.images_idle.append(pygame.transform.scale(
                pygame.image.load(settings.mystery_block_images[i]),
                (self.settings.mystery_block_width,
                 self.settings.mystery_block_height)
            ))

        self.is_empty = False
        self.index = 0
        self.tick_time_limit = settings.mystery_block_TBF

        if is_invisible:
            self.initial_image = self.initial_image.copy()
            self.initial_image.fill((255, 255, 255, 0), None, pygame.BLEND_RGBA_MULT)

        self.sound = mixer.Sound(settings.mystery_block_sound)
        self.image = self.images_idle[0]
        self.rect = self.image.get_rect()

    def update(self):
        if not self.is_empty:
            # update idle frames
            self.iterate_index(len(self.images_idle))
            self.image = self.images_idle[self.index]

    def set_empty(self):
        self.stored_item = self.settings.mystery_block_possible_items['NONE']
        self.is_empty = True
        self.is_hittable = False
        self.image = self.empty_image

    def collision_check(self, sprite_object):
        if self.is_hittable:
            # TODO: JL Note - may need to check corner top collisions
            did_collide = self.rect.collidepoint(sprite_object.rect.midtop)
            if did_collide:
                # TODO - figure out if need to adjust collided object physics
                if not self.is_empty:
                    # Animate Contained Sprite to Appear
                    self.make_item_appear()

                    # Play Sounds
                    self.sound.play()

                    # Change To Empty
                    self.set_empty()
        # else:
        # if collides with bottom and empty, force mario back down

    def make_item_appear(self):
        # TODO: animate sprite to appear in if/else below
        #   Move sprite up until bottom of sprite is at top of block
        obj = None
        if self.stored_item == self.settings.mystery_block_possible_items['MUSHROOM']:
            print('Mushroom item appears!')
            obj = Mushroom(self.screen, self.settings)

        elif self.stored_item == self.settings.mystery_block_possible_items['FIRE_FLOWER']:
            print('Flower item appears!')
            obj = Fire_Flower(self.screen, self.settings)

        elif self.stored_item == self.settings.mystery_block_possible_items['ONE_UP']:
            print('1UP item appears!')
            obj = Mushroom(self.screen, self.settings, is_one_up=True)

        elif self.stored_item == self.settings.mystery_block_possible_items['STAR']:
            print('Star item appears!')
            obj = Star(self.screen, self.settings)
        else:
            # shouldn't be empty!
            print('WARNING - mystery block missing item')
        self.animate_internal_object(obj)

    def iterate_index(self, max_index):
        time = pygame.time.get_ticks() - self.last_tick
        if time > self.tick_time_limit:
            self.index += 1
            self.last_tick = pygame.time.get_ticks()
        if self.index == max_index:
            self.index = 0
