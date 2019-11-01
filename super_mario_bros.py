# Ryan Chen - 893219394
#
# 10/11/19 initial creation - RC
# 10/17/19 added code to test mario star coin and fire flower - RC

import pygame
import sys
import time
from pygame.sprite import Group

import game_functions as gf
import map_generator as map
from settings import Settings
from game_state import Game_State
from mario import Mario
from star import Star
from coin import Coin
from fire_flower import Fire_Flower
from flag import Flag


def run():
    # Initialization
    pygame.init()
    settings = Settings()
    state = Game_State()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Super Mario Bros")
    bg_color = settings.bg_color

    clock = pygame.time.Clock()

    mario = Mario(screen, settings)

    pygame.mixer.music.load("Sounds/overworld.mp3")
    pygame.mixer.music.play()


    # Groups
    map_group = Group()
    block_group = Group()
    floor_group = Group()
    pipe_group = Group()
    enemy_group = Group()
    powerup_group = Group()
    fireball_group = Group()
    dead_group = Group()

    map.generate_map(screen, settings, map_group, floor_group, pipe_group, block_group, enemy_group)
    f = Flag(screen, settings, 198 * settings.block_width, 13 * settings.block_height)
    f.add(map_group)





    pipesprites = pipe_group.sprites()



    # Game Loop
    while state.running:
        clock.tick(60)

        gf.check_events(state, mario, screen, settings, fireball_group, map_group)
        # Update here
        if not mario.is_dead:
            gf.update(screen, settings, mario, map_group, floor_group, pipe_group, block_group, enemy_group, powerup_group, fireball_group, dead_group, f)



            # Display here
        gf.update_screen(screen, settings, mario, map_group, floor_group, pipe_group, block_group, enemy_group, powerup_group, fireball_group, dead_group, f)

    pygame.quit()
    sys.exit()


run()
