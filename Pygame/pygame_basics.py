import pygame
import sys
import time


pygame.init()
screen = pygame.display.set_mode((500, 500))

# Rect(left, top, width, height) -> Rect
i = 0
strt_time = time.time()
strt_time_1 = time.time()
rect = pygame.Rect(0,0,50,50)
screen_rect = screen.get_rect()
rect.center = screen_rect.center
speed = 10
move = "horizontal"

while True:
    
    screen.fill((255, 255, 255))
    if time.time() - strt_time >= 0.1:
        x, y = rect.center
        if move == "horizontal":
            if x > screen_rect.width:
                x = 0
            if x < 0:
                x = screen_rect.width
            rect.center = (x+speed, y)
        else:
            if y > screen_rect.height:
                y = 0
            if y < 0:
                y = screen_rect.height
            rect.center = (x, y+speed)
        strt_time = time.time()
    # if time.time() - strt_time_1 >= 2:
    #     speed += 10
    #     strt_time_1 = time.time()
    pygame.draw.rect(screen, (255,0,0), rect)

    # if time.time() - strt_time >= 0.5:
        # if i == 0:
            # screen.fill((255, 255, 255))
            # i = 1
        # else:
            # screen.fill((0, 0, 0))
            # i = 0
        # strt_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if speed > 0:
                    speed = -speed
                move = "horizontal"
            if event.key == pygame.K_RIGHT:
                if speed < 0:
                    speed = -speed
                move = "horizontal"
            if event.key == pygame.K_DOWN:
                if speed < 0:
                    speed = -speed
                move = "vertical"
            if event.key == pygame.K_UP:
                if speed > 0:
                    speed = -speed
                move = "vertical"

    pygame.display.flip()

