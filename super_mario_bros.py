# Ryan Chen - 893219394
#
# 10/11/19 initial creation

import pygame
import sys
import time

from settings import Settings
from mario import Mario
from star import Star


def run():
    # Initialization
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Super Mario Bros")
    bg_color = settings.bg_color

    clock = pygame.time.Clock()

    mario = Mario(screen, settings)
    star = Star(screen, settings)
    star.current_rect.center = screen.get_rect().center

    # Game Loop
    running = True
    while running:
        clock.tick(60)

        # Temporary exit code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update here
        mario.update()
        star.update()

        # Display here
        screen.fill(settings.bg_color)
        star.draw()
        mario.draw()

        pygame.display.flip()

    pygame.quit()
    sys.exit()


run()
