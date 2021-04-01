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
    max_tps = 100

    #Constant values
    y = 10
    x = 0
    score = 1
    body = []
    direction = "down"
    global screen

    while True:
        height = random.randint(0,1920)
        width = random.randint(0,1080)
        #Checking height and width to spawn apple at right place
        if height%10 == 0 and width%10 == 0:
            break
        else:
            continue
    food = pygame.Rect(height,width,10,10)
    snake = pygame.Rect(800,250,10,10)
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
                    x = -10
                    y = 0
                    direction = "left"
                if keys[pygame.K_d]:
                    x = 10
                    y = 0
                    direction = "right"
            elif direction == "left" or direction == "right":
                if keys[pygame.K_w]:
                    y = -10
                    x = 0
                    direction = "up"
                if keys[pygame.K_s]:
                    y = 10
                    x = 0
                    direction = "down"
            
        snake.y += y
        snake.x += x
        time.sleep(0.05)
        #Creating apple after eating
        if snake.y == width and snake.x == height:
            score +=1
            while True:
                height = random.randint(0,1920)
                width = random.randint(0,1080)
                if height%10 == 0 and width%10 == 0:
                    food = pygame.Rect(height,width,10,10)
                    break
                else:
                    continue
        #This should be deleted #So why is it here?
        if snake.x > 1921:
            snake.x = 0
        if snake.x < 0:
            snake.x = 1920
        if snake.y < 0:
            snake.y = 1080
        if snake.y > 1080:
            snake.y = 0

        screen.fill((0,0,0))
        pygame.draw.rect(screen,(0,255,0),snake)
        snake_body(snake,body,score)
        pygame.draw.rect(screen,(255,0,0),food)
        pygame.display.flip()