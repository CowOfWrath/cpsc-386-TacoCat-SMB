# Ryan Chen - 893219394
#
# 10/18/2019 - RC
#   Initial file creation
#   Added key listener
# 10/27/2019 - Jeffrey
#   Block Collision Checks

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
        # set max jump height from first time
        if mario.is_jumping == False and mario.is_falling == False:
            mario.set_max_jump_height()
            mario.is_jumping = True
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
        # mario.jump = False
        mario.is_falling = True
        mario.is_jumping = False
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
                if mario.rect.centery > e.rect.centery:
                    e.kill()
                else:
                    mario.dead = True # need to add code for killing and animating mario death
            if mario.state == 1 and not mario.shrink:
                if mario.rect.centery > e.rect.centery:
                    e.kill()
                else:
                    mario.shrink = True
            if mario.state == 2 and not mario.shrink:
                if mario.rect.centery > e.rect.centery:
                    e.kill()
                else:
                    mario.shrink = True
            if mario.state == 3:
                e.kill()
            if mario.state == 4:
                e.kill()

def mario_block_collide(mario, block):
    if (mario.rect.bottom >= block.rect.top and
            ((block.rect.left <= mario.rect.left <= block.rect.right) or
             (block.rect.left <= mario.rect.right <= block.rect.right)) and
            mario.rect.top < block.rect.bottom):
        mario.rect.bottom = block.rect.top - 1
        mario.is_falling = False
        mario.jump = False
        return True
    return False


def mario_pipe_collide(mario, pipe):
    if (mario.rect.bottom >= pipe.rect.top and
            ((pipe.rect.left <= mario.rect.left <= pipe.rect.right) or
             (pipe.rect.left <= mario.rect.right <= pipe.rect.right)) and
            mario.rect.top < pipe.rect.bottom):
        mario.rect.bottom = pipe.rect.top - 1
        mario.is_falling = False
        mario.jump = False
        return True
    return False


def mario_floor_collide(mario, floor):
    if (mario.rect.bottom >= floor.rect.top and
            ((floor.rect.left <= mario.rect.left <= floor.rect.right) or
             (floor.rect.left <= mario.rect.right <= floor.rect.right)) and
            mario.rect.top < floor.rect.bottom):
        mario.rect.bottom = floor.rect.top - 1
        mario.is_falling = False
        mario.jump = False
        return True
    return False


def mario_wall_collide(mario, wall):
    #left side of wall
    if ( mario.move_right and mario.rect.right >= wall.rect.left and
            (wall.rect.top < mario.rect.centery < wall.rect.bottom) and mario.rect.left < wall.rect.left
            and not mario.hit_wall):
        print('collision w/ left side')
        # mario.rect.x = wall.rect.left - mario.rect.w - 2
        # mario.rect.x = wall.rect.right + 1
        mario.rect.right = wall.rect.left - 1
        mario.hit_wall = True
        return True
    elif ( mario.move_left and mario.rect.left <= wall.rect.right and
            (wall.rect.top < mario.rect.centery < wall.rect.bottom) and mario.rect.right > wall.rect.right
            and not mario.hit_wall):
        print('collision w/ right side')
        #mario.rect.x = wall.rect.left - mario.rect.w - 1
        mario.rect.left = wall.rect.right + 1
        mario.hit_wall = True
        return True
    return False


def mario_block_bottom_collide(mario, block):
    if (mario.rect.top <= block.rect.bottom and
            (block.rect.left <= mario.rect.centerx <= block.rect.right or
            block.rect.left <= mario.rect.left <= block.rect.right or
            block.rect.left <= mario.rect.right <= block.rect.right) and
            mario.rect.centery > block.rect.centery):
        #mario.rect.y = block.rect.bottom + mario.rect.h
        mario.rect.top = block.rect.bottom + 1
        mario.is_falling = True
        mario.is_jumping = False
        return True
    return False


def mario_block_collision(mario, floor_group, pipe_group, block_group, map_group):
    mg = pygame.sprite.Group(mario)

    # Check if Hit a wall
    mario.hit_wall = False
    floor_wall_hits = pygame.sprite.groupcollide(mg, floor_group, False, False, collided=mario_wall_collide)
    block_wall_hits = pygame.sprite.groupcollide(mg, block_group, False, False, collided=mario_wall_collide)
    pipe_wall_hits = pygame.sprite.groupcollide(mg, pipe_group, False, False, collided=mario_wall_collide)

    if block_wall_hits or pipe_wall_hits or floor_wall_hits:
        print('collided to wall')
        return

    # Bottom of Block Collision
    block_hits = pygame.sprite.groupcollide(mg, block_group, False, False, collided=mario_block_bottom_collide)
    if block_hits:
        for blocks in block_hits.values():
            for block in blocks:
                print('collided to bottom of a block')
                block.break_block(map_group=map_group, rubble_group=pygame.sprite.Group())
        return

    # LANDING ON LOGIC
    mario.is_falling = True
    if not floor_wall_hits:
        floor_hits = pygame.sprite.groupcollide(mg, floor_group, False, False, collided=mario_floor_collide)
        # if floor_hits:
        #     # print(floor_hits)
        #     mario.is_falling = False
        #     mario.jump = False
        #     for floors in floor_hits.values():
        #         for flr in floors:
        #             #mario.y = flr.rect.top - mario.rect.h
        #             mario.rect.bottom = flr.rect.top - 1
        #             # mg.empty()
        #             return

    if mario.is_falling:
        block_hits = pygame.sprite.groupcollide(mg, block_group, False, False, collided=mario_block_collide)
        pipe_hits = pygame.sprite.groupcollide(mg, pipe_group, False, False, collided=mario_pipe_collide)
        # if block_hits:
        #     # print(block_hits)
        #     mario.is_falling = False
        #     mario.jump = False
        #     for blocks in block_hits.values():
        #         for b in blocks:
        #             #mario.y = b.rect.top - mario.rect.h
        #             mario.rect.bottom = b.rect.top - 1
        #             # mg.empty()
        #             return
        # elif pipe_hits and not pipe_wall_hits:
        #     print(pipe_hits)
        #     mario.is_falling = False
        #     mario.jump = False
        #     for pipes in pipe_hits.values():
        #         for p in pipes:
        #             #mario.y = p.rect.top - mario.rect.h
        #             mario.rect.bottom = p.rect.top - 1
        #             # mg.empty()
        #             return

    # Clear mario group so no duplication
    mg.empty()



def check_collisions(settings, mario, map_group, floor_group, pipe_group,block_group, enemy_group, powerup_group, fireball_group):
    mario_block_collision(mario, floor_group, pipe_group, block_group, map_group)
    collide_enemies(mario, enemy_group, fireball_group)

def update(screen, settings, mario, map_group, floor_group, pipe_group,block_group, enemy_group, powerup_group, fireball_group):
    map_group.update()
    mario.update(map_group)
    check_collisions(settings, mario, map_group, floor_group, pipe_group, block_group, enemy_group, powerup_group, fireball_group)


def update_screen(screen, settings, mario, map_group, floor_group, pipe_group, block_group, enemy_group, powerup_group, fireball_group):
    screen.fill(settings.bg_color)
    map_group.draw(screen)
    mario.draw()
    pygame.display.flip()