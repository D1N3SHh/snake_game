#new game module

import pygame
import sys

pygame.init()
def run():
    box = pygame.Rect(600,250,7,7)
    screen = pygame.display.set_mode((1200,500))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            box.y -= 1
        if keys[pygame.K_s]:
            box.y += 1
        if keys[pygame.K_a]:
            box.x -= 1
        if keys[pygame.K_d]:
            box.x += 1

        screen.fill((0,0,0))
        pygame.draw.rect(screen,(0,255,0),box)
        pygame.display.flip()