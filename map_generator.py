# Ryan Chen - 893219394
#
# 10/23/2019 - RC
#   Initial File Creation
#   Created for world 1-1

import pygame
from pygame.sprite import Sprite
from floor import Floor
from pipe import Pipe

class BG(Sprite):
    def __init__(self, screen, settings):
        super(BG, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load("Images/map_1_1.png")
        self.rect = self.image.get_rect()
        self.rect.width = self.rect.width * self.settings.image_scale
        self.rect.height = self.rect.height * self.settings.image_scale
        self.image = pygame.transform.scale(self.image,
                                            (self.rect.width, self.rect.height))

    def draw(self):
        self.screen.blit(self.image, self.rect)


def generate_floor(screen, settings, map_group):
    for i in range(0, 69):
        # level 15 and 16
        f = Floor(screen, settings)
        f.rect.top = 13 * settings.floor_height
        f.rect.left = i * settings.floor_width
        fl = Floor(screen, settings)
        fl.rect.top = 14 * settings.floor_height
        fl.rect.left = i * settings.floor_width
        # print('floor top: ' + str(f.rect.top))
        # print('floor x,y: ' + str(f.rect.x) + ', ' + str(f.rect.y))
        f.add(map_group)
        fl.add(map_group)
    for i in range(71,86):
        f = Floor(screen, settings)
        f.rect.top = 13 * settings.floor_height
        f.rect.left = i * settings.floor_width
        fl = Floor(screen, settings)
        fl.rect.top = 14 * settings.floor_height
        fl.rect.left = i * settings.floor_width
        f.add(map_group)
        fl.add(map_group)
    for i in range(89,153):
        f = Floor(screen, settings)
        f.rect.top = 13 * settings.floor_height
        f.rect.left = i * settings.floor_width
        fl = Floor(screen, settings)
        fl.rect.top = 14 * settings.floor_height
        fl.rect.left = i * settings.floor_width
        f.add(map_group)
        fl.add(map_group)
    for i in range(155,224):
        f = Floor(screen, settings)
        f.rect.top = 13 * settings.floor_height
        f.rect.left = i * settings.floor_width
        fl = Floor(screen, settings)
        fl.rect.top = 14 * settings.floor_height
        fl.rect.left = i * settings.floor_width
        f.add(map_group)
        fl.add(map_group)

    # Overworld Pipes
    p =  Pipe(screen, settings)
    p.set_position(11, 28)
    p.add(map_group)

    p = Pipe(screen, settings, height_factor=3)
    p.set_position(10, 38)
    p.add(map_group)

    p = Pipe(screen, settings, height_factor=4)
    p.set_position(9, 46)
    p.add(map_group)

    # 58,12 pipe
    p = Pipe(screen, settings, height_factor=4)
    p.set_position(9, 57)
    p.add(map_group)

    p = Pipe(screen, settings)
    p.set_position(11, 163)
    p.add(map_group)

    p = Pipe(screen, settings)
    p.set_position(11, 179)
    p.add(map_group)

    # TODO: Generate Underworld Floors and Pipes


    
#def generate_blocks(map_group, block_group):
    # 17,9 mystery block (coin)
    # 21,9 brick
    # 22,9 mystery block (mushroom)
    # 23,9 brick
    # 23,5 mystery block (fire flower)
    # 24,9 mystery block (coin)
    # 25,9 brick
    # 65,8 hiddent block (1up shroom)
    # 78,9 brick
    # 79,9 mysteryblock (mushroom)
    # 80,9 brick
    # 81,5 brick
    # 82,5 brick
    # 83,5 brick
    # 84,5 brick
    # 85,5 brick
    # 86,5 brick
    # 87,5 brick
    # 88,5 brick
    # 92,5 brick
    # 93,5 brick
    # 94,5 brick
    # 95,9 multi hit block
    # 95,5 mysterblock (coin)
    # 101,9 brick
    # 102,9 brick(star)
    # 107,9 mystery block (coin)
    # 110,9 mystery block (coin)
    # 110,5 mystery block (mushroom)
    # 113,9 mystery block (coin)
    # 119,9 brick
    # 122,5 brick
    # 123,5 brick
    # 124,5 brick
    # 129,5brick
    # 130,9 brick
    # 130,5 mysteryblock (coin)
    # 131,9, brick
    # 131,5 mysteryblock (coin)
    # 132,5 brick
    #
    # 135,12 block
    # 136,12 block
    # 136,11 block
    # 137,12 block
    # 137,11 block
    # 137,10 block
    # 138,12 block
    # 138,11 block
    # 138,10 block
    # 138,9  block
    #
    # 141,12 block
    # 141,11 block
    # 141,10 block
    # 141,9  block
    # 142,12 block
    # 142,11 block
    # 142,10 block
    # 143,12 block
    # 143,11 block
    # 144,12 block
    #
    # 149,12 block
    # 150,12 block
    # 150,11 block
    # 151,12 block
    # 151,11 block
    # 151,10 block
    # 152,12 block
    # 152,11 block
    # 152,10 block
    # 152,9  block
    # 153,12 block
    # 153,11 block
    # 153,10 block
    # 153,9  block
    #
    # 156,12 block
    # 156,11 block
    # 156,10 block
    # 156,9  block
    # 157,12 block
    # 157,11 block
    # 157,10 block
    # 158,12 block
    # 158,11 block
    # 159,12 block
    #
    # 169,9 brick
    # 170,9 brick
    # 171,9 mystery block (coin)
    # 172,9 brick
    #
    # 182,12 block
    # 183,12 block
    # 183,11 block
    # 184,12 block
    # 184,11 block
    # 184,10 block
    # 185,12 block
    # 185,11 block
    # 185,10 block
    # 185,9 block
    # 186,12 block
    # 186,11 block
    # 186,10 block
    # 186,9 block
    # 186,8 block
    # 187,12 block
    # 187,11 block
    # 187,10 block
    # 187,9 block
    # 187,8 block
    # 187,7 block
    # 188,12 block
    # 188,11 block
    # 188,10 block
    # 188,9 block
    # 188,8 block
    # 188,7 block
    # 188,6 block
    # 189,12 block
    # 189,11 block
    # 189,10 block
    # 189,9 block
    # 189,8 block
    # 189,7 block
    # 189,6 block
    # 189,5 block
    # 190,12 block
    # 190,11 block
    # 190,10 block
    # 190,9 block
    # 190,8 block
    # 190,7 block
    # 190,6 block
    # 190,5 block
    #
    # 199,12 block






#def generate_entities():
    # 23,12 goomba
    # 41,12 goomba
    # 52,12 goomba
    # 54,12 goomba
    # 81,4  goomba
    # 83,4  goomba
    # 98,12 goombga
    # 100,12 goomba
    # 108,12 koopa
    # 115,12 goomba
    # 117,12 goomba
    # 125,12 goomba
    # 127,12 goomba
    # 130,12 goomba
    # 132,12 goomba
    # 175,12 goomba
    # 177,12 goomba




def generate_map(screen, settings, map_group, block_group, enemy_group):
    bg = BG(screen, settings)
    bg.add(map_group)
    generate_floor(screen, settings, map_group)
    #generate_blocks()
    #generate_entities()


