# simple snake game made using pygame
# authors: D1N3SHh, Naris404, dzideekk
# https://github.com/D1N3SHh/snake_game


# main menu module
import main

# libraries
import pygame
import sys
import random
import time

pygame.init()

# rotating function
def rotate(texture, direction="up"):
    if direction == "left":
        surf = pygame.transform.rotate(texture,90)
    elif direction == "right":
        surf = pygame.transform.rotate(texture,270)
    elif direction == "down":
        surf = pygame.transform.rotate(texture,180)
    else:
        surf = texture
    return surf


# corner rotating function
def rotate_corner(texture, previous_direction, new_direction):

    if (previous_direction == "up" and new_direction == "right") or (previous_direction == "left" and new_direction == "down"):
        surf = texture
    if (previous_direction == "up" and new_direction == "left") or (previous_direction == "right" and new_direction == "down"):
        surf = pygame.transform.rotate(texture, 270)
    if (previous_direction == "down" and new_direction == "right") or (previous_direction == "left" and new_direction == "up"):
        surf = pygame.transform.rotate(texture, 90)
    if (previous_direction == "down" and new_direction == "left") or (previous_direction == "right" and new_direction == "up"):
        surf = pygame.transform.rotate(texture, 180)

    try:
        return surf
    except:
        pass


# snake printing and self colision detection function
def snake_body(head, body, body_direction, score=0):
    global screen, surface_body, surface_tail, direction, active_corners, previous_direction, death
    
    # colision detection
    if head in body:
        death = True

    # body length
    if len(body) > score:
        del(body[0])

    # deleting inactive corners
    for corner in list(active_corners):
         if str(corner) not in str(body):
             del(active_corners[corner])

    # body direction
    body_direction[str(head)] = direction

    # body printing
    for part in body:

        # tail
        if part == body[0]:
            surf = surface_tail
            surf = rotate(surf, body_direction[str(part)])
                    
        # corners
        elif str(part) in active_corners:
            surf = active_corners[str(part)]
            
        # body
        else:
            surf = surface_body
            surf = rotate(surf, body_direction[str(part)])

        try:
            rect = surf.get_rect()
            rect.x = part.x
            rect.y = part.y
        except:
            rect = pygame.Rect(part.x, part.y, 40, 40)

        # pushing on screen
        try:
            screen.blit(surf, rect)
        except:
            surf = surface_body
            surf = rotate(surf, body_direction[str(part)])
            screen.blit(surf, rect)
        
    # previous values
    previous_direction = direction

    # add new element
    body.append(pygame.Rect(head))


# apple spawning and colision detection function
def apple_functions(head,apple):
    global screen, score

    # "is eaten" detection or first iteration
    if score == 0 or head == apple:
        score = score + 1
        spawn = True
    else:
        spawn = False

    # apple spawning function
    while spawn:
        height = random.randint(0,1080)
        width = random.randint(0,1920)
        
        # checking height and width to spawn apple at right place
        if (height%40 == 0 and width%40 == 0) and (height != 1080 and width != 1920):
            break
        else:
            continue

    # apple returning
    surface_food = pygame.image.load("assets/apple.png")
    apple = surface_food.get_rect()
    apple.x = width
    apple.y = height
    return apple


# main function
def run():

    pygame.init()

    # tickrate values
    clock = pygame.time.Clock()
    delta = 0.0
    max_tps = 100

    # start variables
    global score, direction, active_corners, previous_direction, death
    score = 0
    y = 0
    x = 0
    death = False
    first_game = True
    change_direction = False
    running = True
    active_corners = {}
    body = []
    body_direction = {}
    direction = "None"
    previous_direction = "None"
    keys = None

    # pygame variables
    global screen, surface_body, body_texture, surface_tail, tail
    screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
    font = pygame.font.Font('freesansbold.ttf', 50)
    death_screen_font = pygame.font.Font('freesansbold.ttf', 170)
    controls = pygame.image.load('assets/controls.png')
    death_screen = pygame.image.load("assets/death_screen.png")
    surface_background = pygame.image.load("assets/game_background.png")
    rect_background = surface_background.get_rect()
    apple = pygame.Rect(40,40,40,40)
    surface_food = pygame.image.load("assets/apple.png")
    surface_head = pygame.image.load("assets/head.png")
    snake = surface_head.get_rect()
    snake.x = 960
    snake.y = 560
    surface_body = pygame.image.load("assets/body.png")
    body_texture = surface_body.get_rect()
    surface_tail = pygame.image.load("assets/tail.png")
    tail = surface_tail.get_rect()
    surface_corner = pygame.image.load('assets/corner.png')


    # main loop
    while running:

        # checking output keys to exit program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        # tickrate
        delta += clock.tick()/1000.0
        while delta > 1 / max_tps:
            delta -= 1 / max_tps

            # snake turning
            keys = pygame.key.get_pressed()

            if direction == "down" or direction == "up" or direction == "None":
                if keys[pygame.K_a]:
                    x = -40
                    y = 0
                    direction = "left"
                    change_direction = True
                    first_game = False
                if keys[pygame.K_d]:
                    x = 40
                    y = 0
                    direction = "right"
                    change_direction = True
                    first_game = False
            if direction == "left" or direction == "right" or direction == "None":
                if keys[pygame.K_w]:
                    y = -40
                    x = 0
                    direction = "up"
                    change_direction = True
                    first_game = False
                if keys[pygame.K_s]:
                    y = 40
                    x = 0
                    direction = "down"
                    change_direction = True
                    first_game = False

        # corners position and directions
        if change_direction:
            surf = surface_corner
            surf = rotate_corner(surf, previous_direction, direction)
            active_corners[str(snake)] = surf
            change_direction = False

        # new head position
        time.sleep(0.1)
        snake.y += y
        snake.x += x

        # band colison detection
        if snake.x >= 1920:
            death = True
        if snake.x < 0:
            death = True
        if snake.y < 0:
            death = True
        if snake.y >= 1080:
            death = True

        # background
        screen.blit(surface_background,rect_background)

        # showing controls guide on first game
        if first_game:
            x = 0
            y = 0
            screen.blit(controls, (0,0))

        # showing death screen
        elif death:
            x = 0
            y = 0
            screen.blit(death_screen, (0,0))
            # score printing
            score_counter = death_screen_font.render("Score: " + str(score - 1), True, (0,0,0))
            screen.blit(score_counter, (590,760))
            if keys[pygame.K_SPACE]:
                running = False
                pygame.quit()

        # normal iteration
        else:

            # body drawing and self colision detection
            snake_body(snake,body,body_direction,score)

            # head drawing
            surf = rotate(surface_head,direction)
            screen.blit(surf,snake)

            # apple spawning and colision detection function
            try:
                apple = apple_functions(snake,apple)
            except:
                pass
            screen.blit(surface_food,apple)

            # score printing
            score_counter = font.render("Score: " + str(score - 1), True, (0,0,0))
            screen.blit(score_counter, (80,80))

        # frame printing
        try:
            pygame.display.flip()
        except:
            break


# init function
if __name__ == "__main__":
    run()