# Ryan Chen - 893219394
#
# 10/11/19 Initial creation - RC
# 10/17/19 - RC
#   Added settings for star, coin, and fire flower
#   Added image scaling

class Settings:
    def __init__(self):
        self.IMAGE_PATH = self.BASE_PATH + '/images/'


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

        # Brick Settings
        self.brick_width = 8 * self.image_scale
        self.brick_height = 8 * self.image_scale
        self.brick_image = self.IMAGE_PATH + 'brick.png'
        # Underground Brick Settings
        self.brick_ug_image = self.IMAGE_PATH + 'brick_ug.png'
