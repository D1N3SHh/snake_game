#new game module

# libraries
import pygame
import sys
import random
import time

pygame.init()

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

#Apple spawning and colision detection function
def apple_functions(head,apple):
    global screen, score

    #"is eaten" detection or first iteration
    if score == 0 or head == apple:
        score = score + 1
        spawn = True
    else:
        spawn = False

    #Apple spawning function
    while spawn:
        height = random.randint(0,1080)
        width = random.randint(0,1920)
        
        #Checking height and width to spawn apple at right place
        if height%40 == 0 and width%40 == 0:
            if height != 1080 and width != 1920:
                break
            else:
                continue
        else:
            continue

    #Apple returning
    apple = pygame.Rect(width,height,40,40)
    return apple

#Main function
def run():

    #Tickrate values
    clock = pygame.time.Clock()
    delta = 0.0
    max_tps = 100

    #start variables
    global score
    global screen
    y = 0
    x = 0
    body = []
    direction = "None"
    score = 0
    first_game = True

    #pygame variables
    snake = pygame.Rect(1000,520,40,40)
    screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
    apple = pygame.Rect(40,40,40,40)
    font = pygame.font.Font('freesansbold.ttf', 38)
    controls = pygame.image.load('assets/controls.png')
    keys = None

    #Main loop
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

            if direction == "down" or direction == "up" or direction == "None":
                if keys[pygame.K_a]:
                    x = -40
                    y = 0
                    direction = "left"
                    first_game = False
                if keys[pygame.K_d]:
                    x = 40
                    y = 0
                    direction = "right"
                    first_game = False
            if direction == "left" or direction == "right" or direction == "None":
                if keys[pygame.K_w]:
                    y = -40
                    x = 0
                    direction = "up"
                    first_game = False
                if keys[pygame.K_s]:
                    y = 40
                    x = 0
                    direction = "down"
                    first_game = False

        #New head position
        time.sleep(0.08)
        snake.y += y
        snake.x += x

        #Band colison detection
        if snake.x >= 1920:
            sys.exit(0)
        if snake.x < 0:
            sys.exit(0)
        if snake.y < 0:
            sys.exit(0)
        if snake.y >= 1080:
            sys.exit(0)

        #Clearing screen
        screen.fill((0,0,0))

        #Showing controls guide on first game
        if first_game:
            x = 0
            y = 0
            screen.blit(controls, (0,0))
        else:

            #Body drawing and self colision detection
            snake_body(snake,body,score)

            #Head drawing
            pygame.draw.rect(screen,(0,0,255),snake)

            #Apple spawning and colision detection function
            try:
                apple = apple_functions(snake,apple)
            except:
                pass
            pygame.draw.rect(screen,(255,0,0),apple)

            #Score printing
            score_counter = font.render("Score: " + str(score - 1), True, (255,255,255))
            screen.blit(score_counter, (100,60))

        #Frame printing
        pygame.display.flip()

# init function
if __name__ == "__main__":
    run()