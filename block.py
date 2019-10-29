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

    def __init__(self, screen, settings, is_underground=False, is_stairs=False):
        super(Block, self).__init__()
        self.screen = screen
        self.settings = settings
        self.is_underground = is_underground
        self.last_tick = pygame.time.get_ticks()
        self.index = 0
        self.initial_image = None

        # Block States
        self.is_hittable = True
        self.is_broken = False
        # TODO: add break block code
        self.break_sound = mixer.Sound(settings.break_brick_sound)


        # initial block image
        if is_stairs:
            self.initial_image = pygame.transform.scale(
                image.load(settings.block_stairs_image),
                (self.settings.brick_width,
                 self.settings.brick_height)
            )
        elif is_underground:
            self.initial_image = pygame.transform.scale(
                image.load(settings.brick_ug_image),
                (self.settings.brick_width,
                 self.settings.brick_height)
            )

        else:
            self.initial_image = pygame.transform.scale(
                image.load(settings.brick_image),
                (self.settings.brick_width,
                 self.settings.brick_height)
            )

        self.image = self.initial_image
        self.rect = self.image.get_rect()

        self.collision_pts = self.get_collision_points()

    def set_position(self, top, left):
        self.rect.top = top * self.settings.block_height
        self.rect.left = left * self.settings.block_width

    def get_collision_points(self):
        self.collision_pts = {
            "topSide": [self.rect.topleft, self.rect.midtop, self.rect.topright],
            "rightSide": [self.rect.topright, self.rect.midright, self.rect.bottomright],
            "botSide": [self.rect.bottomleft, self.rect.midbottom, self.rect.bottomright],
            "leftSide": [self.rect.topleft, self.rect.midleft, self.rect.bottomleft],
        }
        return self.collision_pts

    def collision_check(self, sprite_object):
        pass

    def handle_bottom_collision(self, map_group, rubble_group=None):
        if self.is_hittable and not self.is_broken:
            self.break_block(map_group=map_group, rubble_group=rubble_group)

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

    def break_block(self, rubble_group, map_group):
        if self.is_hittable:
            self.is_broken = True
            speeds = [(-15, 5), (-10, 5), (10, 5), (15, 5)]
            for speed in speeds:
                left = False
                if speed[0] < 0:
                    left = True
                rubble = BrickRubblePiece(self.screen, self.settings, is_left=left, x=speed[0], y=speed[1] )
                rubble_group.add(rubble)
                map_group.add(rubble)
            self.break_sound.play()
            self.kill()



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
    def __init__(self, screen, settings, is_left=True, x=0, y=0):
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
        self.rect.x, self.rect.y = x, y
        self.x_speed = settings.brick_rubble_speed_x
        self.y_speed = settings.brick_rubble_speed_y

    def update(self):
        # update image
        self.iterate_index(len(self.frames_list))
        self.image = self.frames_list[self.f_index]
        #update pos
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.x_speed > 0:
            self.x_speed -= 1
        else:
            self.x_speed += 1
        if self.rect.y > self.screen.get_height():
            self.kill()

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
    def __init__(self, screen, settings, coins=0, is_underground=False):
        super(CoinBlock, self).__init__(screen, settings, is_underground)
        self.num_coins_left = coins
        self.coins = []
        self.empty_image = pygame.transform.scale(
            image.load(settings.block_empty_image),
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

    def __init__(self, screen, settings, stored_item='', is_invisible=False, is_underground=False):
        super(MysteryBlock, self).__init__(screen, settings, is_underground)
        self.empty_image = pygame.transform.scale(
            image.load(settings.block_empty_image),
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
            self.initial_image = pygame.Surface([settings.brick_width, settings.brick_height], pygame.SRCALPHA, 32).convert_alpha()
            # TODO - remove this fill statement for hidden block
            self.initial_image.fill((255, 255, 255, 50))
            length = len(self.images_idle)
            self.images_idle.clear()
            for i in range(length):
                self.images_idle.append(self.initial_image)

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

        elif self.stored_item == self.settings.mystery_block_possible_items['COIN']:
            print('Flower item appears!')
            obj = Coin(self.screen, self.settings)

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


class BrickMysteryBlock(MysteryBlock):
    def __init__(self, screen, settings, stored_item='', is_underground=False):
        super(BrickMysteryBlock, self).__init__(screen, settings, stored_item=stored_item, is_invisible=False, is_underground=is_underground)

        # initial block image
        if is_underground:
            self.initial_image = pygame.transform.scale(
                image.load(settings.brick_ug_image),
                (self.settings.brick_width,
                 self.settings.brick_height)
            )
        else:
            self.initial_image = pygame.transform.scale(
                image.load(settings.brick_image),
                (self.settings.brick_width,
                 self.settings.brick_height)
            )

        self.images_idle.clear()
        self.images_idle = [self.initial_image]
        self.image = self.images_idle[0]
        self.rect = self.image.get_rect()

