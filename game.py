#new game module

import pygame
import sys
import random
import time

#pygame.init()

#Snake printing and self colision detection function
def snake_body(head,body,score=0):
    global screen
    #colision detection
    if head in body:
        print("game over")
        print("score: ",score)
        sys.exit(0)

    #body length
    body.append(pygame.Rect(head))
    if len(body) > score:
        del(body[0])

    #body printing
    for part in body:
        pygame.draw.rect(screen, (0,255,0),part)

def run():

    #Tickrate values
    clock = pygame.time.Clock()
    delta = 0.0
    max_tps = 60

    #Constant values
    y = 0
    x = 50
    score = 1
    body = []
    direction = "right"
    global screen

    while True:
        height = random.randint(0,1920)
        width = random.randint(0,1080)
        #Checking height and width to spawn apple at right place
        if height%50 == 0 and width%50 == 0:
            break
        else:
            continue
    food = pygame.Rect(height,width,50,50)
    snake = pygame.Rect(0,0,50,50)
    screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
    while True:
        #Checking output keys to exit program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        #Tickrate
        delta += clock.tick()/1000.0
        while delta > 1 / max_tps:
            delta -= 1 / max_tps

            #Snake turning
            keys = pygame.key.get_pressed()
            if direction == "down" or direction == "up":
                if keys[pygame.K_a]:
                    x = -50
                    y = 0
                    direction = "left"
                if keys[pygame.K_d]:
                    x = 50
                    y = 0
                    direction = "right"
            elif direction == "left" or direction == "right":
                if keys[pygame.K_w]:
                    y = -50
                    x = 0
                    direction = "up"
                if keys[pygame.K_s]:
                    y = 50
                    x = 0
                    direction = "down"
        time.sleep(0.2)
        snake.y += y
        snake.x += x
        
        #Creating apple after eating
        if snake.y == width and snake.x == height:
            score +=1
            while True:
                height = random.randint(0,1920)
                width = random.randint(0,1080)
                if height%50 == 0 and width%50 == 0:
                    food = pygame.Rect(height,width,50,50)
                    break
                else:
                    continue
                
        #Band colison detection
        if snake.x > 1920:
            sys.exit(0)
        if snake.x < 0:
            sys.exit(0)
        if snake.y < 0:
            sys.exit(0)
        if snake.y > 1080:
            sys.exit(0)

        screen.fill((0,0,0))
        pygame.draw.rect(screen,(122,0,122),snake)
        snake_body(snake,body,score)
        pygame.draw.rect(screen,(255,0,0),food)
        pygame.display.flip()