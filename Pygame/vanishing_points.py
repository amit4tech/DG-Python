import pygame
import sys
import time

def draw_grid(surface):
    pygame.draw.line(surface, (0,0,0), (200, 0), (200, 600), 5)
    pygame.draw.line(surface, (0,0,0), (400, 0), (400, 600), 5)
    pygame.draw.line(surface, (0,0,0), (0, 200), (600, 200), 5)
    pygame.draw.line(surface, (0,0,0), (0, 400), (600, 400), 5)


pygame.init()
screen = pygame.display.set_mode((600, 600))
circles = []

while True:

    screen.fill((255, 255, 255))
    temp_circles = []
    for circle in circles:
        x, y, t = circle
        if time.time() - t <= 1:
            pygame.draw.circle(screen, (255, 0, 0), (x,y), 5)
            temp_circles.append(circle)
    
    circles = temp_circles
    # draw_grid(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     circle_center = event.pos
        #     # print(circle_center)
        #     circles.append(circle_center)

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            t = time.time()
            circles.append((x, y, t))

    pygame.display.flip()

