import pygame
from pygame.sprite import Sprite


class Fireball(Sprite):
    # Class to manage fireballs

    def __init__(self, screen, settings, xpos, ypos):
        # Create fireball where Mario currently is
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.facing_left = False
        self.fall = False
        self.bounces = 0
        self.explode = False
        self.index = 0
        self.last_tick = pygame.time.get_ticks()
        self.name = "Fireball"

        self.image = pygame.transform.scale(pygame.image.load("Images/fireball_1.png"),
                                            (self.settings.fireball_width, self.settings.fireball_height))
        self.rect = self.image.get_rect()
        self.rect.left = xpos
        self.rect.top = ypos

        # Images for fireball
        self.images = []
        self.images.extend([pygame.transform.scale(pygame.image.load("Images/fireball_1.png"),
                                                   (self.settings.fireball_width, self.settings.fireball_height)),
                            pygame.transform.scale(pygame.image.load("Images/fireball_2.png"),
                                                   (self.settings.fireball_width, self.settings.fireball_height)),
                            pygame.transform.scale(pygame.image.load("Images/fireball_3.png"),
                                                   (self.settings.fireball_width, self.settings.fireball_height)),
                            pygame.transform.scale(pygame.image.load("Images/fireball_4.png"),
                                                   (self.settings.fireball_width, self.settings.fireball_height))])
        self.explode_frames = []
        self.explode_frames.extend([pygame.transform.scale(pygame.image.load("Images/explode_0.png"),
                                                           (self.settings.fireball_width,
                                                            self.settings.fireball_height)),
                                    pygame.transform.scale(pygame.image.load("Images/explode_1.png"),
                                                           (self.settings.fireball_width,
                                                            self.settings.fireball_height)),
                                    pygame.transform.scale(pygame.image.load("Images/explode_2.png"),
                                                           (self.settings.fireball_width,
                                                            self.settings.fireball_height))])

        # Store location
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.fireball_speed = settings.fireball_speed

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.bounces == 4:
            self.explode = True
        if self.explode:
            self.iterate_index(len(self.explode_frames))
            self.image = self.explode_frames[self.index]
        else:
            self.iterate_index(len(self.images))
            self.image = self.images[self.index]
        if self.facing_left:
            self.rect.centerx -= self.settings.fireball_speed
        else:
            self.rect.centerx += self.settings.fireball_speed

    def iterate_index(self, max):
        time = pygame.time.get_ticks() - self.last_tick
        if time > 50:
            self.index += 1
            self.last_tick = pygame.time.get_ticks()

            # temporarily placed movement in iterate, should belong in its own function
            # if self.fall:
            #     self.rect.centery += self.settings.fireball_jump
            # else:
            #     self.rect.centery -= self.settings.fireball_jump
        if self.index == max:
            self.index = 0
            self.bounces += 1
            if self.explode:
                self.kill()
            # self.fall = not self.fall
