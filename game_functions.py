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
        mario.facing_left = False
        mario.move_left = False
        mario.move_right = True

    elif event.key == pygame.K_LEFT:
        print("left down")
        mario.facing_left = True
        mario.move_left = True
        mario.move_right = False

    if event.key == pygame.K_UP:
        print("up down")
        mario.jump = True
    elif event.key == pygame.K_DOWN:
        print("down down")
        mario.crouch = True

    if event.key == pygame.K_LCTRL:
        mario.run = True


def check_keyup(event, mario):
    if event.key == pygame.K_RIGHT:
        print("right up")
        mario.move_right = False
    elif event.key == pygame.K_LEFT:
        print("left up")
        mario.move_left = False

    if event.key == pygame.K_UP:
        print("up up")
        mario.jump = False
    elif event.key == pygame.K_DOWN:
        print("down up")
        mario.crouch = False

    if event.key == pygame.K_LCTRL:
        mario.run = False

def collide_enemies(mario, enemy_group, fireball_group):
    collisions = pygame.sprite.groupcollide(enemy_group, fireball_group, True, True)
    for e in enemy_group:
        if pygame.sprite.collide_rect(mario, e):
            if mario.state == 0:
                if mario.rect.centery > e.rect.centery
                    e.kill()
                else:
                    mario.dead = True # need to add code for killing and animating mario death
            if mario.state == 1 and not mario.shrink:
                if mario.rect.centery > e.rect.centery
                    e.kill()
                else:
                    mario.shrink = True
            if mario.state == 2 and not mario.shrink:
                if mario.rect.centery > e.rect.centery
                    e.kill()
                else:
                    mario.shrink = True
            if mario.state == 3:
                e.kill()
            if mario.state == 4:
                e.kill()


def update(screen, settings, mario, map_group, block_group, enemy_group, powerup_group, fireball_group):
    # for x in map_group:
    #     x.update()
    map_group.update()
    mario.update(map_group)
    # for x in block_group:
    #     x.update()
    # for x in enemy_group:
    #     x.update()
    # for x in powerup_group:
    #     x.update()
    # for x in fireball_group:
    #     x.update()



def update_screen(screen, settings, mario, map_group, block_group, enemy_group, powerup_group, fireball_group):
    screen.fill(settings.bg_color)
    map_group.draw(screen)
    mario.draw()
    # for x in map_group:
    #     x.draw()

    # for x in block_group:
    #     x.draw()
    # for x in enemy_group:
    #     x.draw()
    # for x in powerup_group:
    #     x.draw()
    # for x in fireball_group:
    #     x.draw()

    # map_group.draw(screen)
    # block_group.draw(screen)
    # enemy_group.draw(screen)
    # powerup_group.draw(screen)
    #
    #fireball_group.draw(screen)
    pygame.display.flip()