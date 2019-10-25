# Jeffrey Lo
#
# 10/18/19 Initial creation - JL
import pygame
from pygame import image
from pygame import mixer
from pygame.sprite import Sprite


class Pipe(Sprite):
    def __init__(self, screen, settings, destinationPoint=None, isHorizontal=False):
        super(Pipe, self).__init__()
        self.screen = screen
        self.settings = settings
        self.destination = destinationPoint
        self.is_horizontal = isHorizontal

        self.sound = mixer.Sound(settings.pipe_sound)

        self.current_image = pygame.transform.scale(
            image.load(settings.pipe_image),
            (self.settings.pipe_width,
             self.settings.pipe_height)
        )
        self.current_rect = self.current_image.get_rect()

    def check_entered(self, mario):
        # returns None if no-entry or tuple with teleport spawn location
        # check if no-entry pipe
        if not self.destination:
            return None

        pts = None
        collision_pts = {
            "topSide":[mario.current_rect.topleft, mario.current_rect.midtop, mario.current_rect.topright],
            "rightSide":[mario.current_rect.topright, mario.current_rect.midright, mario.current_rect.bottomright],
            "botSide": [mario.current_rect.botleft, mario.current_rect.midbottom, mario.current_rect.botright]
        }

        if (not self.is_horizontal) and mario.crouch:
            pts = collision_pts["botSide"]
        elif self.is_horizontal and (not mario.facing_left):
            pts = collision_pts["rightSide"]

        if pts:
            if self.current_rect.collidepoint(pts[0]) and self.current_rect.collidepoint(pts[1]) and self.current_rect.collidepoint(pts[2]):
                # TODO - JL consider mario animation?
                return self.destination