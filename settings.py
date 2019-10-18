# Ryan Chen - 893219394
# Jeffrey Lo
# 10/11/19 Initial creation - RC
# 10/17/19 - RC
#   Added settings for star, coin, and fire flower
#   Added image scaling
# 10/18/19 - JL
#   added settings for floors, bricks
#   added paths for sound and images
from os.path import abspath, dirname


class Settings:
    def __init__(self):
        self.BASE_PATH = abspath(dirname(__file__))
        self.IMAGE_PATH = self.BASE_PATH + '/images/'
        self.SOUND_PATH = self.BASE_PATH + '/sound/'

        # General Settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (0, 0, 0)
        self.image_scale = 8

        # Mario Settings
        self.bm_width = 8 * self.image_scale
        self.bm_height = 16 * self.image_scale
        self.sm_width = 8 * self.image_scale
        self.sm_height = 8 * self.image_scale

        # Star Settings
        self.star_width = 8 * self.image_scale
        self.star_height = 8 * self.image_scale
        self.star_speed = 1 * self.image_scale
        self.star_jump = 8 * self.image_scale

        # Coin Settings
        self.coin_width = 8 * self.image_scale
        self.coin_height = 8 * self.image_scale

        # Fire Flower Settings
        self.fire_flower_width = 8 * self.image_scale
        self.fire_flower_height = 8 * self.image_scale

        # Floor Settings
        self.floor_width = 8 * self.image_scale
        self.floor_height = 8 * self.image_scale
        self.floor_image = self.IMAGE_PATH + 'floor.png'
        self.floor_ug_image = self.IMAGE_PATH + 'floor_ug.png'

        # Brick Settings
        self.brick_width = 8 * self.image_scale
        self.brick_height = 8 * self.image_scale
        self.brick_image = self.IMAGE_PATH + 'brick.png'
        # Underground Brick Settings
        self.brick_ug_image = self.IMAGE_PATH + 'brick_ug.png'

        # Block Settings
        self.block_width = 8 * self.image_scale
        self.block_height = 8 * self.image_scale
        self.block_empty = self.IMAGE_PATH + 'block_empty.png'

        # Block Sounds
        self.coin_block_sound = self.SOUND_PATH + 'coin.wav'
