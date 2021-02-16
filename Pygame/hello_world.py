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
while True:
    
    screen.fill((255, 255, 255))
    if time.time() - strt_time >= 0.1:
        x, y = rect.center
        if x > screen_rect.width:
            x = 0
        if x < 0:
            x = screen_rect.width
        rect.center = (x+speed, y)
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
            if event.key == pygame.K_RIGHT:
                if speed < 0:
                    speed = -speed
            
    pygame.display.flip()

