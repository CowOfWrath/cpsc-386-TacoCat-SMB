# Ryan Chen - 893219394
#
# 10/23/2019 - RC
#   Initial File Creation
#   Created for world 1-1

import pygame
from pygame.sprite import Sprite
from floor import Floor

class BG(Sprite):
    def __init__(self, screen, settings):
        super(BG, self).__init__()
        self.screen = screen
        self.settings = settings

        self.current_image = pygame.image.load("Images/map_1_1.png")
        self.current_rect = self.current_image.get_rect()
        self.current_rect.width = self.current_rect.width * self.settings.image_scale
        self.current_rect.height = self.current_rect.height * self.settings.image_scale
        self.current_image = pygame.transform.scale(self.current_image,
                                                    (self.current_rect.width, self.current_rect.height))

    def draw(self):
        self.screen.blit(self.current_image, self.current_rect)


def generate_floor(screen, settings, map_group):
    for i in range(0, 69):
        # level 15 and 16
        f = Floor(screen, settings)
        f.current_rect.top = 13 * settings.floor_height
        f.current_rect.left = i * settings.floor_width
        fl = Floor(screen, settings)
        fl.current_rect.top = 14 * settings.floor_height
        fl.current_rect.left = i * settings.floor_width
        f.add(map_group)
        fl.add(map_group)
    for i in range(71,86):
        f = Floor(screen, settings)
        f.current_rect.top = 13 * settings.floor_height
        f.current_rect.left = i * settings.floor_width
        fl = Floor(screen, settings)
        fl.current_rect.top = 14 * settings.floor_height
        fl.current_rect.left = i * settings.floor_width
        f.add(map_group)
        fl.add(map_group)
    for i in range(89,153):
        f = Floor(screen, settings)
        f.current_rect.top = 13 * settings.floor_height
        f.current_rect.left = i * settings.floor_width
        fl = Floor(screen, settings)
        fl.current_rect.top = 14 * settings.floor_height
        fl.current_rect.left = i * settings.floor_width
        f.add(map_group)
        fl.add(map_group)
    for i in range(155,224):
        f = Floor(screen, settings)
        f.current_rect.top = 13 * settings.floor_height
        f.current_rect.left = i * settings.floor_width
        fl = Floor(screen, settings)
        fl.current_rect.top = 14 * settings.floor_height
        fl.current_rect.left = i * settings.floor_width
        f.add(map_group)
        fl.add(map_group)
    
#def generate_blocks():


#def generate_entities():


def generate_map(screen, settings, map_group, block_group, enemy_group):
    bg = BG(screen, settings)
    bg.add(map_group)
    generate_floor(screen, settings, map_group)
    #generate_blocks()
    #generate_entities()


