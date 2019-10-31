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
        # mario.is_falling = True
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


# entity collides w/ top of block or pipe
def entity_block_pipe_collide(entity, block):
    if (entity.rect.bottom >= block.rect.top and
            ((block.rect.left <= entity.rect.left <= block.rect.right) or
             (block.rect.left <= entity.rect.right <= block.rect.right)) and
            entity.rect.top < block.rect.bottom):
        entity.rect.bottom = block.rect.top - 1
        # TODO edit entity falling status if needed
        return True
    return False


def entity_floor_collide(entity, floor):
    if (entity.rect.bottom >= floor.rect.top and
            (floor.rect.left <= entity.rect.centerx <= floor.rect.right) and
            entity.rect.top < floor.rect.top):
        entity.y = floor.rect.top - entity.rect.h
        # TODO edit entity falling status if needed
        return True
    return False


def entity_wall_collide(entity, wall):
    if (entity.rect.right >= wall.rect.left and
            (wall.rect.top < entity.rect.centery < wall.rect.bottom) and entity.rect.left < wall.rect.left
            and not entity.hit_wall and not entity.facing_left):
        # print('collision w/ left side')
        entity.rect.right = wall.rect.left - 1
        # TODO code to change entity direction
        return True
    elif (entity.rect.left <= wall.rect.right and
            (wall.rect.top < entity.rect.centery < wall.rect.bottom) and entity.rect.right > wall.rect.right
            and not entity.hit_wall and entity.facing_left):
        # print('collision w/ right side')
        entity.rect.left = wall.rect.right + 1
        # TODO code to change entity direction
        return True
    return False


def mario_block_collide(mario, block):
    if (mario.rect.bottom >= block.rect.top and
            ((block.rect.left <= mario.rect.left <= block.rect.right) or
             (block.rect.left <= mario.rect.right <= block.rect.right)) and
            mario.rect.top < block.rect.top):
        print('mario landed on block')
        mario.rect.bottom = block.rect.top - 1
        mario.is_falling = False
        mario.jump = False
        return True
    return False


def mario_pipe_collide(mario, pipe):
    if (mario.rect.bottom >= pipe.rect.top and
            ((pipe.rect.left <= mario.rect.left <= pipe.rect.right) or
             (pipe.rect.left <= mario.rect.right <= pipe.rect.right)) and
            mario.rect.top < pipe.rect.bottom and not mario.is_jumping):
        print('mario landed on pipe')
        mario.rect.bottom = pipe.rect.top - 1
        # mario.y = mario.rect.y
        mario.set_max_jump_height()
        mario.is_falling = False
        mario.jump = False
        return True
    return False


def mario_floor_collide(mario, floor):
    if (mario.rect.bottom >= floor.rect.top and
            (floor.rect.left <= mario.rect.centerx <= floor.rect.right) and
            mario.rect.top < floor.rect.top):
        # mario.rect.bottom = floor.rect.top - 1
        # print('mario landed on floor')
        mario.y = floor.rect.top - mario.rect.h

        mario.is_falling = False
        mario.jump = False
        return True
    return False


def mario_wall_collide(mario, wall):
    #left side of wall
    if (mario.rect.right >= wall.rect.left and
            (wall.rect.top <= mario.rect.centery <= wall.rect.bottom or
             wall.rect.topleft[1] <= mario.rect.topright[1] < wall.rect.bottomleft[1] or
             wall.rect.topleft[1] < mario.rect.bottomright[1] <= wall.rect.bottomleft[1]) and
            mario.rect.left < wall.rect.left
            and not mario.hit_wall):
        print('collision w/ left side')
        mario.rect.x = wall.rect.left - mario.rect.w - 1
        mario.x = mario.rect.x
        # mario.rect.x = wall.rect.right + 1
        # mario.rect.right = wall.rect.left - 1
        mario.hit_wall = True
        return True
    elif (mario.rect.left <= wall.rect.right and
            (wall.rect.top <= mario.rect.centery <= wall.rect.bottom or
             wall.rect.topright[1] <= mario.rect.topleft[1] < wall.rect.bottomright[1] or
             wall.rect.topright[1] < mario.rect.bottomleft[1] <= wall.rect.bottomright[1]) and mario.rect.right > wall.rect.right and not mario.hit_wall):
        print('collision w/ right side')
        print('mario falling ' + str(mario.is_falling) )
        print('wall tr: ' + str(wall.rect.topright) + 'br: ' + str(wall.rect.bottomright))
        print('mario tl: ' + str(mario.rect.topleft))
        print('wall tr: ' + str(wall.rect.topright) + 'br: ' + str(wall.rect.bottomright))
        print('mario bl: ' + str(mario.rect.bottomleft))

        mario.rect.x = wall.rect.right + 1
        mario.x = mario.rect.x
        # mario.rect.left = wall.rect.right + 1
        mario.hit_wall = True
        return True
    return False


def mario_block_bottom_collide(mario, block):
    if (mario.rect.top <= block.rect.bottom and
            block.rect.left <= mario.rect.centerx <= block.rect.right and
            (block.rect.left <= mario.rect.left < block.rect.right or
             block.rect.left < mario.rect.right <= block.rect.right) and
            mario.rect.centery > block.rect.centery and mario.is_jumping):
        #mario.rect.y = block.rect.bottom + mario.rect.h
        mario.rect.top = block.rect.bottom + 1
        print('collided bottom')
        mario.is_falling = True
        mario.is_jumping = False
        return True
    return False


def mario_block_collision(mario, floor_group, pipe_group, block_group, map_group):
    mg = pygame.sprite.Group(mario)

    # Check if Hit a wall
    mario.hit_wall = False

    block_wall_hits = pygame.sprite.groupcollide(mg, block_group, False, False, collided=mario_wall_collide)
    pipe_wall_hits = pygame.sprite.groupcollide(mg, pipe_group, False, False, collided=mario_wall_collide)
    if (block_wall_hits or pipe_wall_hits) and not mario.is_jumping:
        print('exited with wall')
        if pipe_wall_hits:
            mario.use_idle_image()
        mario.is_falling = True
        return

    floor_wall_hits = pygame.sprite.groupcollide(mg, floor_group, False, False, collided=mario_wall_collide)
    if floor_wall_hits:
        return

    # Bottom of Block Collision
    block_hits = pygame.sprite.groupcollide(mg, block_group, False, False, collided=mario_block_bottom_collide)
    if block_hits:
        for blocks in block_hits.values():
            for block in blocks:
                print('collided to bottom of a block')
                if mario.state == 0 or mario.state == 3:
                    block.handle_bottom_collision(map_group=map_group)
                else:
                    block.handle_bottom_collision(map_group=map_group, can_break_block=True)
        return

    # LANDING ON LOGIC
    mario.is_falling = True
    floor_hits = pygame.sprite.groupcollide(mg, floor_group, False, False, collided=mario_floor_collide)
    if floor_hits:
        return

    if mario.is_falling:
        block_hits = pygame.sprite.groupcollide(mg, block_group, False, False, collided=mario_block_collide)
        if block_hits:
            print('fell on block')
            return

        pipe_hits = pygame.sprite.groupcollide(mg, pipe_group, False, False, collided=mario_pipe_collide)
        if pipe_hits:
            print('fell on pipe')
            return

    # Clear mario group so no duplication
    mg.empty()
    # END mario_block_collision()


def enemy_block_collision(enemy_group, floor_group, pipe_group, block_group, map_group ):
    # TODO enable enemy collisions when needed
    if False:
        # Check for Wall Collision
        enemy_floor_wall_check = pygame.sprite.groupcollide(enemy_group, floor_group, False, False, collided=entity_wall_collide)
        if enemy_floor_wall_check:
            return
        e_block_wall_hits = pygame.sprite.groupcollide(enemy_group, block_group, False, False, collided=entity_wall_collide)
        e_pipe_wall_hits = pygame.sprite.groupcollide(enemy_group, pipe_group, False, False, collided=entity_wall_collide)

        # LANDING Logic Check
        e_floor_hits = pygame.sprite.groupcollide(enemy_group, floor_group, False, False, collided=entity_floor_collide)
        if e_floor_hits:
            return

        e_block_hits = pygame.sprite.groupcollide(enemy_group, block_group, False, False, collided=entity_block_pipe_collide)
        if e_block_hits:
            return
        e_pipe_hits = pygame.sprite.groupcollide(enemy_group, pipe_group, False, False, collided=entity_block_pipe_collide)
        if e_pipe_hits:
            return
    # END entity_block_collision


def item_block_collision(item_group, floor_group, pipe_group, block_group, map_group):
    # TODO: Add some check for if item is moving
    if False:
        # Wall Collisions
        item_floor_wall_check = pygame.sprite.groupcollide(item_group, floor_group, False, False, collided=entity_wall_collide)
        if item_floor_wall_check:
            return
        i_block_wall_hits = pygame.sprite.groupcollide(item_group, block_group, False, False, collided=entity_wall_collide)
        i_pipe_wall_hits = pygame.sprite.groupcollide(item_group, pipe_group, False, False, collided=entity_wall_collide)

        # LANDING Logic Check
        i_floor_hits = pygame.sprite.groupcollide(item_group, floor_group, False, False, collided=entity_floor_collide)
        if i_floor_hits:
            return
        i_block_hits = pygame.sprite.groupcollide(item_group, block_group, False, False, collided=entity_block_pipe_collide)
        if i_block_hits:
            return
        i_pipe_hits = pygame.sprite.groupcollide(item_group, pipe_group, False, False, collided=entity_block_pipe_collide)
        if i_pipe_hits:
            return
    # end item collision check


def check_collisions(settings, mario, map_group, floor_group, pipe_group,block_group, enemy_group, powerup_group, fireball_group):
    # mario environment collisions
    mario_block_collision(mario, floor_group, pipe_group, block_group, map_group)
    # mario enemy collisions
    collide_enemies(mario, enemy_group, fireball_group)
    # entity (enemies/items) environment collisions
    enemy_block_collision(enemy_group, floor_group, pipe_group, block_group, map_group)
    item_block_collision(powerup_group, floor_group, pipe_group, block_group, map_group)

def update(screen, settings, mario, map_group, floor_group, pipe_group,block_group, enemy_group, powerup_group, fireball_group):
    map_group.update()
    mario.update(map_group)
    check_collisions(settings, mario, map_group, floor_group, pipe_group, block_group, enemy_group, powerup_group, fireball_group)


def update_screen(screen, settings, mario, map_group, floor_group, pipe_group, block_group, enemy_group, powerup_group, fireball_group):
    screen.fill(settings.bg_color)
    map_group.draw(screen)
    mario.draw()
    pygame.display.flip()