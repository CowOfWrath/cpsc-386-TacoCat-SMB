# Ryan Chen - 893219394
#
# 10/17/19 Initial creation
#   Added basic settings and states
#   Added image handling and placeholders

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, screen, settings):
        super(Star, self).__init__()
        self.screen = screen
        self.settings = settings

        self.facing_left = False
        self.fall = False
        self.index = 0
        self.last_tick = pygame.time.get_ticks()

        self.current_image = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                    (self.settings.star_width, self.settings.star_height))

        self.current_rect = self.current_image.get_rect()

        self.images = []
        self.images.append(pygame.transform.scale(pygame.image.load("Images/star_1.png"),
                                                  (self.settings.star_width, self.settings.star_height)))
        self.images.append(pygame.transform.scale(pygame.image.load("Images/star_2.png"),
                                                  (self.settings.star_width, self.settings.star_height)))
        self.images.append(pygame.transform.scale(pygame.image.load("Images/star_3.png"),
                                                  (self.settings.star_width, self.settings.star_height)))
        self.images.append(pygame.transform.scale(pygame.image.load("Images/star_4.png"),
                                                  (self.settings.star_width, self.settings.star_height)))

    def draw(self):
        self.screen.blit(pygame.transform.flip(self.current_image, self.facing_left, False), self.current_rect)

    def update(self):
        self.iterate_index(len(self.images))
        self.current_image = self.images[self.index]
        if self.facing_left:
            self.current_rect.centerx -= self.settings.star_speed
        else:
            self.current_rect.centerx += self.settings.star_speed

        # Need to move this to an external game function to handle collsion with blocks as well
        if self.current_rect.right >= self.screen.get_rect().right:
            self.facing_left = True
        if self.current_rect.left <= 0:
            self.facing_left = False

    def iterate_index(self, max):
        time = pygame.time.get_ticks() - self.last_tick
        if time > 100:
            self.index += 1
            self.last_tick = pygame.time.get_ticks()

            # temporarily placed movement in iterate, should belong in its own function
            if self.fall:
                self.current_rect.centery += self.settings.star_jump
            else:
                self.current_rect.centery -= self.settings.star_jump
        if self.index == max:
            self.index = 0
            self.fall = not self.fall
