# Ryan Chen - 893219394
#
# 10/11/19 Initial creation

class Settings:
    def __init__(self):
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
