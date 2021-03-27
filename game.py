#new game module

import pygame
import sys
import random

pygame.init()

def run():

    #Tickrate values
    clock = pygame.time.Clock()
    delta = 0.0
    max_tps = 10

    y = 1
    x = 0
    height = random.randint(0,1920)
    width = random.randint(0,1080)
    food = pygame.Rect(height,width,25,25)
    snake = pygame.Rect(800,250,50,50)
    screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        #Tickrate
        delta += clock.tick()/1000.0
        while delta > 1 / max_tps:
            delta -= 1 / max_tps

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                y = -1 # -1
                x = 0
            if keys[pygame.K_s]:
                y = 1 # 1
                x = 0
            if keys[pygame.K_a]:
                x = -1 # -1
                y = 0
            if keys[pygame.K_d]:
                x = 1 # 1
                y = 0

        snake.y += y
        snake.x += x

        if snake.y == height:
            print("Done")

        screen.fill((0,0,0))
        pygame.draw.rect(screen,(0,255,0),snake)
        pygame.draw.rect(screen,(255,0,0),food)
        pygame.display.flip()