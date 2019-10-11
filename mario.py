# Ryan Chen - 893219394
#
# 10/11/19 Initial creation
#   Added basic settings and states
#   Added image handling and placeholders

from pygame.sprite import Sprite


class Mario(Sprite):
    def __init__(self, screen, settings):
        super(Mario, self).__init__()
        self.settings = settings
        self.screen = screen

        self.current_width = self.settings.SM_width
        self.current_height = self.settings.SM_height

        # States: sm = 0 | bm = 1 | fm = 2 | smi = 3 | bmi = 4
        self.state = 0
        self.walk = False
        self.jump = False
        self.shrink = False
        self.grow = False
        self.fireball = False
        self.index = 0

        self.current_image = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                    (self.current_width, self.current_height))

        self.current_rect = self.current_image.get_rect()

        # Images for Small Mario
        self.sm_walk = []
        self.sm_walk.append(pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                   (self.settings.sm_width, self.settings.sm_height)))

        self.sm_jump = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                              (self.settings.sm_width, self.settings.sm_height))

        self.sm_grow = []
        self.sm_grow.append(pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                   (self.settings.sm_width, self.settings.sm_height)))

        self.sm_dead = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                              (self.settings.sm_width, self.settings.sm_height))

        # Images for Big Mario
        self.bm_walk = []
        self.bm_walk.append(pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))

        self.bm_jump = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                              (self.settings.bm_width, self.settings.bm_height))

        self.bm_shrink = []
        self.bm_shrink.append(pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                     (self.settings.bm_width, self.settings.bm_height)))

        # Images for Fire Mario
        self.fm_walk = []
        self.fm_walk.append(pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                   (self.settings.bm_width, self.settings.bm_height)))

        self.fm_jump = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                              (self.settings.bm_width, self.settings.bm_height))

        self.fm_throw_fb = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                  (self.settings.bm_width, self.settings.bm_height))

        self.fm_shrink = []
        pygame.transform.scale(pygame.image.load("Images/white.png"),
                               (self.settings.bm_width, self.settings.bm_height))

        # Images for Small Mario Invincible
        self.smi_walk = []
        self.smi_walk.append(pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                    (self.settings.sm_width, self.settings.sm_height)))

        self.smi_jump = pygame.transform.scale(pygame.image.load("Images/white.png"),
                                               (self.settings.sm_width, self.settings.sm_height))

        self.smi_sparkle = []
        self.smi_sparkle.pygame.transform.scale(pygame.image.load("Images/white.png"),
                                                (self.settings.sm_width, self.settings.sm_height))

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
        self.screen.blit(self.image, self.rect)

    def update(self):
        if 0:  # Small Mario
            if self.grow:
                iterate_index(len(self.sm_grow))
                self.current_image = self.sm_grow[self.index]
            elif self.shrink:
                self.current_image = self.sm_dead
            elif self.jump:
                self.current_image = self.sm_jump
            elif self.walk:
                iterate_index(len(self.sm_walk))
                self.current_image = self.sm_walk[self.index]
            else:
                self.current_image = self.sm_walk[0]
        elif 1:  # Big Mario
            if self.shrink:
                iterate_index(len(self.bm_shrink))
                self.current_image = self.bm_shrink[self.index]
            elif self.jump:
                self.current_image = self.bm_jump
            elif self.walk:
                iterate_index(len(self.bm_walk))
                self.current_image = self.bm_walk[self.index]
            else:
                self.current_image = self.bm_walk[0]
        elif 2:  # Fire Mario
            if self.shrink:
                iterate_index(len(self.fm_shrink))
                self.current_image = self.fm_shrink
            elif self.fireball:
                self.current_image = self.fm_throw_fb
                self.fireball = False
            elif self.jump:
                self.current_image = self.fm_jump
            elif self.walk:
                iterate_index(len(self.fm_walk))
                self.current_image = self.fm_walk[self.index]
            else:
                self.current_image = self.fm_walk[0]
        elif 3:  # Small Mario Invincible
            if self.grow:
                iterate_index(len(self.smi_grow))
                self.current_image = self.smi_grow[self.index]
            elif self.jump:
                self.current_image = self.smi_jump
            elif self.walk:
                iterate_index(len(self.smi_walk))
                self.current_image = self.smi_walk[self.index]
            else:
                iterate_index(len(self.smi_sparkle))
                self.current_image = self.smi_sparkle[0]
        elif 4:  # Big Mario Invinicble
            if self.jump:
                self.current_image = self.bmi_jump
            elif self.walk:
                iterate_index(len(self.bmi_walk))
                self.current_image = self.bmi_walk[self.index]
            else:
                iterate_index(len(self.bmi_sparkle))
                self.current_image = self.bmi_sparkle[0]
        else:  # reset state to default on error
            self.state = 0
            self.jump = False
            self.shrink = False
            self.index = 0


def iterate_index(max):
    self.index += 1
    if self.index == max:
        self.index = 0
