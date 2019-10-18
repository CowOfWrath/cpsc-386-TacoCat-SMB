# Ryan Chen - 893219394
#
# 10/11/19 initial creation - RC
# 10/17/19 added code to test mario star coin and fire flower - RC

import pygame
import sys
import time

import game_functions as gf
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
    star.current_rect.center = screen.get_rect().center

    coin1 = Coin(screen, settings)
    coin1.idle = False
    coin1.current_rect.centerx = 100

    coin2 = Coin(screen, settings)
    coin2.current_rect.centerx = 200

    ff = Fire_Flower(screen, settings)
    ff.current_rect.centerx = 300

    # Game Loop
    while state.running:
        clock.tick(60)

        # Update here
        gf.check_events(state, mario)
        ff.update()
        star.update()
        coin1.update()
        coin2.update()
        mario.update()

        # Display here
        screen.fill(settings.bg_color)
        coin1.draw()
        coin2.draw()
        ff.draw()
        star.draw()
        mario.draw()

        pygame.display.flip()

    pygame.quit()
    sys.exit()


run()
