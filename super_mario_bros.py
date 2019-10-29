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

    star = Star(screen, settings)
    star.rect.center = screen.get_rect().center

    coin1 = Coin(screen, settings)
    coin1.idle = False
    coin1.rect.centerx = 100

    coin2 = Coin(screen, settings)
    coin2.rect.centerx = 200

    ff = Fire_Flower(screen, settings)
    ff.rect.centerx = 300

    # Groups
    map_group = Group()
    block_group = Group()
    floor_group = Group()
    pipe_group = Group()
    enemy_group = Group()
    powerup_group = Group()
    fireball_group = Group()

    map.generate_map(screen, settings, map_group, floor_group, pipe_group, block_group, enemy_group)


    star.add(map_group)
    ff.add(map_group)
    coin1.add(map_group)
    coin2.add(map_group)
    star.add(powerup_group)
    ff.add(powerup_group)
    coin1.add(powerup_group)
    coin2.add(powerup_group)

    
    pipesprites = pipe_group.sprites()
    
    
    
    # Game Loop
    while state.running:
        clock.tick(60)

        # Update here
        gf.check_events(state, mario)

        gf.check_collisions(settings, mario, map_group, floor_group, pipe_group, block_group, enemy_group, powerup_group, fireball_group)

        gf.update(screen, settings, mario, map_group, floor_group, pipe_group, block_group, enemy_group, powerup_group, fireball_group)
        # ff.update()
        # star.update()
        # coin1.update()
        # coin2.update()
        # mario.update(map_group)
        #block updates
        # for b in block_group.sprites():
        #     b.update()



        # Display here
        gf.update_screen(screen, settings, mario, map_group, floor_group, pipe_group, block_group, enemy_group, powerup_group, fireball_group)
        # screen.fill(settings.bg_color)
        # coin1.draw()
        # coin2.draw()
        # ff.draw()
        # star.draw()
        # mario.draw()

        # pygame.display.flip()

    pygame.quit()
    sys.exit()


run()
