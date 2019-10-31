# Ryan Chen - 893219394
#
# 10/11/19 Initial creation - RC
#   Added basic settings and states
#   Added image handling and placeholders
# 10/17/19 - RC
#   Added some sprites and some state changes
# 10/27/10 - JL
#   Added mario jump
#   Added mario collision flags and logic

import pygame
from pygame.sprite import Sprite


class Mario(Sprite):
    def __init__(self, screen, settings):
        super(Mario, self).__init__()
        self.settings = settings
        self.screen = screen

        # States: sm = 0 | bm = 1 | fm = 2 | smi = 3 | bmi = 4
        self.state = 1
        self.is_dead = False
        self.walk = False
        self.run = False
        self.jump = False
        self.crouch = False
        self.shrink = False
        self.grow = False
        self.fireball = False
        self.facing_left = False
        self.move_right = False
        self.move_left = False
        self.iframes = False
        self.index = 0
        self.last_tick = pygame.time.get_ticks()
        self.once_tick = pygame.time.get_ticks()
        self.invincible_tick = pygame.time.get_ticks()

        # Mario collision Flags
        self.is_falling = True
        self.is_jumping = False
        self.hit_wall = False

        self.image = pygame.transform.scale(pygame.image.load("Images/mario_small_idle.png"),
                                                    (self.settings.sm_width, self.settings.sm_height))

        self.rect = self.image.get_rect()
        self.x = self.settings.sm_width * 3
        self.y = self.settings.sm_height * 12

        self.display_rect = pygame.Rect(0, 0, self.settings.bm_width, self.settings.bm_height)

        # Images for Small Mario
        self.sm_idle = pygame.transform.scale(pygame.image.load("Images/mario_small_idle.png"),
                                              (self.settings.sm_width, self.settings.sm_height))
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
        self.sm_grow.append(pygame.transform.scale(pygame.image.load("Images/mario_small_idle.png"),
                                                   (self.settings.sm_width, self.settings.sm_height)))
        self.sm_grow.append(pygame.transform.scale(pygame.image.load("Images/mario_big_hit.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))
        self.sm_grow.append(pygame.transform.scale(pygame.image.load("Images/mario_big_idle.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))
        self.sm_grow.append(pygame.transform.scale(pygame.image.load("Images/mario_small_idle.png"),
                                                   (self.settings.sm_width, self.settings.sm_height)))
        self.sm_grow.append(pygame.transform.scale(pygame.image.load("Images/mario_big_hit.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))
        self.sm_grow.append(pygame.transform.scale(pygame.image.load("Images/mario_big_idle.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))
        self.sm_grow.append(pygame.transform.scale(pygame.image.load("Images/mario_small_idle.png"),
                                                   (self.settings.sm_width, self.settings.sm_height)))
        self.sm_grow.append(pygame.transform.scale(pygame.image.load("Images/mario_big_hit.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))
        self.sm_grow.append(pygame.transform.scale(pygame.image.load("Images/mario_big_idle.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))

        self.sm_dead = pygame.transform.scale(pygame.image.load("Images/mario_death.png"),
                                              (self.settings.sm_width, self.settings.sm_height))

        # Images for Big Mario
        self.bm_idle = pygame.transform.scale(pygame.image.load("Images/mario_big_idle.png"),
                                              (self.settings.bm_width, self.settings.bm_height))
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
                                                (self.settings.bm_width, self.settings.bm_height))

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
        self.fm_idle = pygame.transform.scale(pygame.image.load("Images/fire_mario_idle.png"),
                                              (self.settings.bm_width, self.settings.bm_height))
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
                                                (self.settings.bm_width, self.settings.bm_height))

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
        self.smi_sparkle.append(pygame.transform.scale(pygame.image.load("Images/small_mario_invincible_1.png"),
                                                       (self.settings.sm_width, self.settings.sm_height)))
        self.smi_sparkle.append(pygame.transform.scale(pygame.image.load("Images/small_mario_invincible_2.png"),
                                                       (self.settings.sm_width, self.settings.sm_height)))
        self.smi_sparkle.append(pygame.transform.scale(pygame.image.load("Images/small_mario_invincible_3.png"),
                                                       (self.settings.sm_width, self.settings.sm_height)))
        self.smi_sparkle.append(pygame.transform.scale(pygame.image.load("Images/small_mario_invincible_4.png"),
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
        self.bmi_sparkle.append(pygame.transform.scale(pygame.image.load("Images/big_mario_invincible_1.png"),
                                                       (self.settings.bm_width, self.settings.bm_height)))
        self.bmi_sparkle.append(pygame.transform.scale(pygame.image.load("Images/big_mario_invincible_2.png"),
                                                       (self.settings.bm_width, self.settings.bm_height)))
        self.bmi_sparkle.append(pygame.transform.scale(pygame.image.load("Images/big_mario_invincible_3.png"),
                                                       (self.settings.bm_width, self.settings.bm_height)))
        self.bmi_sparkle.append(pygame.transform.scale(pygame.image.load("Images/big_mario_invincible_4.png"),
                                                       (self.settings.bm_width, self.settings.bm_height)))
        self.bmi_sparkle.append(pygame.transform.scale(pygame.image.load("Images/big_mario_invincible_5.png"),
                                                       (self.settings.bm_width, self.settings.bm_height)))

    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, self.facing_left, False), self.rect)

    def dead(self):
        self.is_dead = True  # need to add code for killing and animating mario death
        self.image = self.sm_dead
        pygame.mixer.Sound("Sounds/die.wav").play()

    def update(self, map_group):
        if self.rect.bottom >= self.screen.get_rect().bottom:
            self.dead()
            return

        if self.iframes:
            time = pygame.time.get_ticks() - self.invincible_tick
            if time > 1000:
                self.iframes = False
        # Update Movement
        self.walk = False
        if not self.shrink and not self.grow:
            # print("has hit wall: " + str(self.hit_wall))
            if self.move_right and not self.crouch:
                self.walk = True
                if self.hit_wall:
                    print('hitting a wall')
                elif self.x >= self.settings.screen_width / 2:
                    for e in map_group:
                        if self.run:
                            e.rect.x -= self.settings.mario_run
                        else:
                            e.rect.x -= self.settings.mario_walk
                else:
                    if self.run:
                        self.x += self.settings.mario_run
                    else:
                        self.x += self.settings.mario_walk
            elif self.move_left and not self.crouch and self.x > 0:
                self.walk = True
                if self.hit_wall:
                    print('hitting a wall')
                elif self.run:
                    self.x -= self.settings.mario_run
                else:
                    self.x -= self.settings.mario_walk
            # else:
            #     print('no wall hit')

            if self.is_falling:
                self.y += self.settings.gravity
                self.jump = True

            if self.is_jumping:
                if self.y <= self.max_jump_height:
                    self.is_falling = True
                    self.is_jumping = False
                    self.y += self.settings.gravity
                else:
                    self.y -= self.settings.mario_jump
                    self.is_falling = False
                    self.jump = True

        # Update animation states and hitbox and position
        if self.state == 0:  # Small Mario
            if self.grow:  # On mushroom collision set index to 0
                self.iterate_once(len(self.sm_grow))
                temp = self.rect.copy()
                self.image = self.sm_grow[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.bottom = temp.bottom
            elif self.shrink:
                self.image = self.sm_dead
            elif self.jump:
                self.image = self.sm_jump
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
            elif self.walk:
                self.iterate_index(len(self.sm_walk))
                self.image = self.sm_walk[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
            else:
                self.image = self.sm_idle
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
        elif self.state == 1:  # Big Mario
            if self.shrink:  # On enemy collsion set indeox to 0
                self.iterate_once(len(self.bm_shrink))
                temp = self.rect.copy()
                self.image = self.bm_shrink[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.bottom = temp.bottom
            elif self.jump:
                self.image = self.bm_jump
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
            elif self.crouch:
                self.image = self.bm_crouch
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
            elif self.walk:
                self.iterate_index(len(self.bm_walk))
                self.image = self.bm_walk[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
            else:
                self.image = self.bm_idle
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
        elif self.state == 2:  # Fire Mario
            if self.shrink:  # On enemy collision set index to 0
                self.iterate_once(len(self.fm_shrink))
                temp = self.rect.copy()
                self.image = self.fm_shrink[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.bottom = temp.bottom
            elif self.fireball:
                self.image = self.fm_throw_fb
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
                self.fireball = False
            elif self.jump:
                self.image = self.fm_jump
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
            elif self.crouch:
                self.image = self.fm_crouch
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
            elif self.walk:
                self.iterate_index(len(self.fm_walk))
                self.image = self.fm_walk[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
            else:
                self.image = self.fm_idle
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
        elif self.state == 3:  # Small Mario Invincible
            if self.grow:  # On mushroom collision set index to 0
                self.iterate_once(len(self.smi_grow))
                temp = self.rect.copy()
                self.image = self.smi_grow[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.bottom = temp.bottom
            elif self.jump:
                self.image = self.smi_jump
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
            elif self.walk:
                self.iterate_index(len(self.smi_walk))
                self.image = self.smi_walk[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
            else:
                self.iterate_index(len(self.smi_sparkle))
                self.image = self.smi_sparkle[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
        elif self.state == 4:  # Big Mario Invinicble
            if self.jump:
                self.image = self.bmi_jump
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
            elif self.walk:
                self.iterate_index(len(self.bmi_walk))
                self.image = self.bmi_walk[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
            else:
                self.iterate_index(len(self.bmi_sparkle))
                self.image = self.bmi_sparkle[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = self.x
                self.rect.y = self.y
        else:  # reset state to default on error (This should never happen)
            self.state = 0
            self.walk = False
            self.jump = False
            self.crouch = False
            self.shrink = False
            self.grow = False
            self.fireball = False
            self.facing_left = False
            self.move_right = False
            self.move_left = False
            self.index = 0

    def set_max_jump_height(self):
        self.max_jump_height = self.rect.y - self.settings.mario_max_jump_height

    def use_idle_image(self):
        # States: sm = 0 | bm = 1 | fm = 2 | smi = 3 | bmi = 4
        if self.state == 0:
            self.image = self.sm_idle
        elif self.state == 1:
            self.image = self.bm_idle
        elif self.state == 2:
            self.image = self.fm_idle
        elif self.state == 3:
            self.image = self.smi_idle
        elif self.state == 4:
            self.image = self.bmi_idle
        else:
            print('impossible state')

    def iterate_index(self, max):
        time = pygame.time.get_ticks() - self.last_tick
        if time > 100:
            self.index += 1
            self.last_tick = pygame.time.get_ticks()
        if self.index == max:
            self.index = 0

    def iterate_once(self, max):
        time = pygame.time.get_ticks() - self.once_tick
        if time > 100:
            self.index += 1
            self.once_tick = pygame.time.get_ticks()
        if self.index == max:
            self.shrink = False
            self.grow = False
            self.state = 0
            self.index = 0