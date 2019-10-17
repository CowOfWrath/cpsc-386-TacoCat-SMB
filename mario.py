# Ryan Chen - 893219394
#
# 10/11/19 Initial creation
#   Added basic settings and states
#   Added image handling and placeholders

import pygame
from pygame.sprite import Sprite


class Mario(Sprite):
    def __init__(self, screen, settings):
        super(Mario, self).__init__()
        self.settings = settings
        self.screen = screen

        self.current_width = self.settings.sm_width
        self.current_height = self.settings.sm_height

        # States: sm = 0 | bm = 1 | fm = 2 | smi = 3 | bmi = 4
        self.state = 0
        self.walk = True
        self.jump = False
        self.crouch = False
        self.shrink = False
        self.grow = False
        self.fireball = False
        self.facing_left = False
        self.index = 0
        self.last_tick = pygame.time.get_ticks()

        self.current_image = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                    (self.current_width, self.current_height))

        self.current_rect = self.current_image.get_rect()

        # Images for Small Mario
        self.sm_walk = []
        self.sm_walk.append(pygame.transform.scale(pygame.image.load("Images/mario_small_walk1.png"),
                                                   (self.settings.sm_width, self.settings.sm_height)))
        self.sm_walk.append(pygame.transform.scale(pygame.image.load("Images/mario_small_walk2.png"),
                                                   (self.settings.sm_width, self.settings.sm_height)))
        self.sm_walk.append(pygame.transform.scale(pygame.image.load("Images/mario_small_walk3.png"),
                                                   (self.settings.sm_width, self.settings.sm_height)))

        self.sm_jump = pygame.transform.scale(pygame.image.load("Images/mario_small_jump.png"),
                                              (self.settings.sm_width, self.settings.sm_height))

        self.sm_grow = []
        self.sm_grow.append(pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                   (self.settings.sm_width, self.settings.sm_height)))

        self.sm_dead = pygame.transform.scale(pygame.image.load("Images/mario_death.png"),
                                              (self.settings.sm_width, self.settings.sm_height))

        # Images for Big Mario
        self.bm_walk = []
        self.bm_walk.append(pygame.transform.scale(pygame.image.load("Images/mario_big_walk1.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))
        self.bm_walk.append(pygame.transform.scale(pygame.image.load("Images/mario_big_walk2.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))
        self.bm_walk.append(pygame.transform.scale(pygame.image.load("Images/mario_big_walk3.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))

        self.bm_jump = pygame.transform.scale(pygame.image.load("Images/mario_big_jump.png"),
                                              (self.settings.bm_width, self.settings.bm_height))

        self.bm_crouch = pygame.transform.scale(pygame.image.load("Images/mario_big_crouch.png"),
                                                (self.settings.sm_width, self.settings.sm_height))

        self.bm_shrink = []
        self.bm_shrink.append(pygame.transform.scale(pygame.image.load("Images/mario_big_idle.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))
        self.bm_shrink.append(pygame.transform.scale(pygame.image.load("Images/mario_big_hit.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))
        self.bm_shrink.append(pygame.transform.scale(pygame.image.load("Images/mario_small_idle.png"),
                                                     (self.settings.sm_width, self.settings.sm_height)))
        self.bm_shrink.append(pygame.transform.scale(pygame.image.load("Images/mario_big_idle.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))
        self.bm_shrink.append(pygame.transform.scale(pygame.image.load("Images/mario_big_hit.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))
        self.bm_shrink.append(pygame.transform.scale(pygame.image.load("Images/mario_small_idle.png"),
                                                     (self.settings.sm_width, self.settings.sm_height)))
        self.bm_shrink.append(pygame.transform.scale(pygame.image.load("Images/mario_big_idle.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))
        self.bm_shrink.append(pygame.transform.scale(pygame.image.load("Images/mario_big_hit.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))
        self.bm_shrink.append(pygame.transform.scale(pygame.image.load("Images/mario_small_idle.png"),
                                                     (self.settings.sm_width, self.settings.sm_height)))

        # Images for Fire Mario
        self.fm_walk = []
        self.fm_walk.append(pygame.transform.scale(pygame.image.load("Images/fire_mario_walk1.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))
        self.fm_walk.append(pygame.transform.scale(pygame.image.load("Images/fire_mario_walk2.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))
        self.fm_walk.append(pygame.transform.scale(pygame.image.load("Images/fire_mario_walk3.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))

        self.fm_jump = pygame.transform.scale(pygame.image.load("Images/fire_mario_jump.png"),
                                              (self.settings.bm_width, self.settings.bm_height))

        # NEED UPDATE - need to look for a fire mario fireball throw image
        self.fm_throw_fb = pygame.transform.scale(pygame.image.load("Images/fire_mario_idle.png"),
                                                  (self.settings.bm_width, self.settings.bm_height))

        self.fm_crouch = pygame.transform.scale(pygame.image.load("Images/fire_mario_crouch.png"),
                                                (self.settings.sm_width, self.settings.sm_height))

        self.fm_shrink = []
        self.fm_shrink.append(pygame.transform.scale(pygame.image.load("Images/fire_mario_idle.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))
        self.fm_shrink.append(pygame.transform.scale(pygame.image.load("Images/fire_mario_hit.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))
        self.fm_shrink.append(pygame.transform.scale(pygame.image.load("Images/fire_mario_hit_idle.png"),
                                                     (self.settings.sm_width, self.settings.sm_height)))
        self.fm_shrink.append(pygame.transform.scale(pygame.image.load("Images/fire_mario_idle.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))
        self.fm_shrink.append(pygame.transform.scale(pygame.image.load("Images/fire_mario_hit.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))
        self.fm_shrink.append(pygame.transform.scale(pygame.image.load("Images/fire_mario_hit_idle.png"),
                                                     (self.settings.sm_width, self.settings.sm_height)))
        self.fm_shrink.append(pygame.transform.scale(pygame.image.load("Images/fire_mario_idle.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))
        self.fm_shrink.append(pygame.transform.scale(pygame.image.load("Images/fire_mario_hit.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))
        self.fm_shrink.append(pygame.transform.scale(pygame.image.load("Images/fire_mario_hit_idle.png"),
                                                     (self.settings.sm_width, self.settings.sm_height)))

        # Images for Small Mario Invincible
        self.smi_walk = []
        self.smi_walk.append(pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                    (self.settings.sm_width, self.settings.sm_height)))

        self.smi_jump = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                               (self.settings.sm_width, self.settings.sm_height))

        self.smi_sparkle = []
        self.smi_sparkle.append(pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                       (self.settings.sm_width, self.settings.sm_height)))

        self.smi_grow = []
        self.smi_grow.append(pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                    (self.settings.sm_width, self.settings.sm_height)))

        # Images for Big Mario Invincible
        self.bmi_walk = []
        self.bmi_walk.append(pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                    (self.settings.bm_width, self.settings.bm_height)))

        self.bmi_jump = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                               (self.settings.bm_width, self.settings.bm_height))

        self.bmi_sparkle = []
        self.bmi_sparkle.append(pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                       (self.settings.bm_width, self.settings.bm_height)))

    def draw(self):
        self.screen.blit(pygame.transform.flip(self.current_image, self.facing_left, False), self.current_rect)

    def update(self):
        if self.state == 0:  # Small Mario
            if self.grow:
                self.iterate_index(len(self.sm_grow))
                self.current_image = self.sm_grow[self.index]
                self.current_rect = self.current_image.get_rect()
            elif self.shrink:
                self.current_image = self.sm_dead
            elif self.jump:
                self.current_image = self.sm_jump
            elif self.walk:
                self.iterate_index(len(self.sm_walk))
                self.current_image = self.sm_walk[self.index]
            else:
                self.current_image = self.sm_walk[0]
        elif self.state == 1:  # Big Mario
            if self.shrink:
                self.iterate_index(len(self.bm_shrink))
                self.current_image = self.bm_shrink[self.index]
                self.current_rect = self.current_image.get_rect()
            elif self.jump:
                self.current_image = self.bm_jump
            elif self.crouch:
                self.current_image = self.bm_crouch
                self.current_rect = self.current_image.get_rect()  # on key release reset the rect
            elif self.walk:
                self.iterate_index(len(self.bm_walk))
                self.current_image = self.bm_walk[self.index]
            else:
                self.current_image = self.bm_walk[0]
        elif self.state == 2:  # Fire Mario
            if self.shrink:
                self.iterate_index(len(self.fm_shrink))
                self.current_image = self.fm_shrink[self.index]
                self.current_rect = self.current_image.get_rect()
            elif self.fireball:
                self.current_image = self.fm_throw_fb
                self.fireball = False
            elif self.jump:
                self.current_image = self.fm_jump
            elif self.crouch:
                self.current_image = self.fm_crouch
                self.current_rect = self.current_image.get_rect()  # on key release reset the rect
            elif self.walk:
                self.iterate_index(len(self.fm_walk))
                self.current_image = self.fm_walk[self.index]
            else:
                self.current_image = self.fm_walk[0]
        elif self.state == 3:  # Small Mario Invincible
            if self.grow:
                self.iterate_index(len(self.smi_grow))
                self.current_image = self.smi_grow[self.index]
                self.current_rect = self.current_image.get_rect()
            elif self.jump:
                self.current_image = self.smi_jump
            elif self.walk:
                self.iterate_index(len(self.smi_walk))
                self.current_image = self.smi_walk[self.index]
            else:
                self.iterate_index(len(self.smi_sparkle))
                self.current_image = self.smi_sparkle[0]
        elif self.state == 4:  # Big Mario Invinicble
            if self.jump:
                self.current_image = self.bmi_jump
            elif self.walk:
                self.iterate_index(len(self.bmi_walk))
                self.current_image = self.bmi_walk[self.index]
            else:
                self.iterate_index(len(self.bmi_sparkle))
                self.current_image = self.bmi_sparkle[0]
        else:  # reset state to default on error
            self.state = 0
            self.jump = False
            self.shrink = False
            self.index = 0

    def iterate_index(self, max):
        time = pygame.time.get_ticks() - self.last_tick
        if time > 100:
            self.index += 1
            self.last_tick = pygame.time.get_ticks()
        if self.index == max:
            self.index = 0
