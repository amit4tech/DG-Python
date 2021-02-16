import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((600, 600))
image = pygame.image.load("C:\\Users\\Manu\\Desktop\\DG_Lectures\\Pygame\\cross.bmp")
resized_image = pygame.transform.scale(image, (200, 200))

while True:
    screen.fill((255, 255, 255))
    rect = pygame.Rect(0, 0, 200, 200)
    screen.blit(resized_image, rect)
    # pygame.draw.rect(screen, (255,0,0), rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()


