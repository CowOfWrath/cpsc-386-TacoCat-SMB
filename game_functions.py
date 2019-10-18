# Ryan Chen - 893219394
#
# 10/18/2019 - RC
#   Initial file creation
#   Added key listener

import pygame


def check_events(state, mario):
    # Check key and mouse events
    for event in pygame.event.get():
        # Quit game events
        if event.type == pygame.QUIT:
            state.running = False
        elif event.type == pygame.KEYDOWN:
            check_keydown(state, event, mario)
        elif event.type == pygame.KEYUP:
            check_keyup(event, mario)


def check_keydown(state, event, mario):
    if event.key == pygame.K_ESCAPE:
        state.running = False

    # Mario movement events
    elif event.key == pygame.K_RIGHT:
        print("right down")
        mario.walk = True
        mario.facing_left = False
        mario.move_left = False
        mario.move_right = True

    elif event.key == pygame.K_LEFT:
        print("left down")
        mario.walk = True
        mario.facing_left = True
        mario.move_left = True
        mario.move_right = False

    if event.key == pygame.K_UP:
        print("up down")
        mario.jump = True
    elif event.key == pygame.K_DOWN:
        print("down down")
        mario.crouch = True


def check_keyup(event, mario):
    if event.key == pygame.K_RIGHT:
        print("right up")
        mario.walk = False
        mario.move_right = False
    elif event.key == pygame.K_LEFT:
        print("left up")
        mario.walk = False
        mario.move_left = False

    if event.key == pygame.K_UP:
        print("up up")
        mario.jump = False
    elif event.key == pygame.K_DOWN:
        print("down up")
        mario.crouch = False
