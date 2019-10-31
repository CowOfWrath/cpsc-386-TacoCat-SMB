 # Rey Vergara

import pygame
from pygame.sprite import Sprite


class Shell(Sprite):

    def __init__(self, screen, settings):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.fall = False
        self.active = False
        self.hit_wall = False
        self.is_dead = False
        self.left = False

        self.image = pygame.transform.scale(pygame.image.load("Images/koopa_shell.png"),
                                            (self.settings.koopa_width, self.settings.koopa_width))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.is_dead:
            return
        if self.active:
            if self.left:
                self.rect.centerx -= 1.5
            else:
                self.rect.centerx += 1.5
