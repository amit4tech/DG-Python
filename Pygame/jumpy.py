import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jump")
clock = pygame.time.Clock()


class Object:
    def __init__(self, midbottom):
        self.rect = pygame.Rect(0, 0, 50 , 100)
        self.rect.midbottom = midbottom
        self.u = 0
        self.t = 0
        self.g = 2
        self.hu = 0

    def jump(self, u=-50):
        if self.rect.bottom + self.u < screen.get_rect().bottom:
            return
        self.u = u
        self.t = 0
        self.hu = 5
        self.move()

    def move(self):
        self.u = self.u + self.g * self.t
        self.t += 1
    
    def update(self):
        if self.rect.bottom + self.u >= screen.get_rect().bottom:
            self.u = 0
            self.hu = 0
            self.rect.bottom = screen.get_rect().bottom
        else:
            self.move()
        self.rect.move_ip(self.hu, self.u)

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

x, y = screen.get_rect().midbottom
obj = Object((x-100, y))

while True:
    clock.tick(20)
    screen.fill((255, 255, 255))
    obj.update()
    obj.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                obj.jump()

    pygame.display.flip()

