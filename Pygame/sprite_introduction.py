import pygame
import sys
import time

class Enemies:

    def __init__(self, no_of_enemies):
        self.enemies = []
        self.hvel = 5
        self.vvel = 20
        for i in range(no_of_enemies):
            enemy = pygame.Rect(0,0,50,30)
            enemy.center = ((i+1)*500//(no_of_enemies+1), 100)
            self.enemies.append(enemy)
        
    def draw(self, screen):

        for enemy in self.enemies:
            pygame.draw.rect(screen, (255,0,0), enemy)   

    def move(self):
        move_down = False
        for enemy in self.enemies:
            if enemy.midright[0] >= 500 or enemy.midleft[0] <= 0:
                self.hvel = -self.hvel
                move_down = True
            enemy.move_ip(self.hvel, 0)
        
        if move_down:
            for enemy in self.enemies:
                enemy.move_ip(0, self.vvel)

class Bullet:

    def __init__(self, x, y):
                
        self.rect = pygame.Rect(0,0,5,10)
        self.rect.center = (x, y)
        self.vel = -10

    def move(self):
        self.rect.move_ip(0, self.vel)
        return self.rect.y >= 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)


class Bullets:
    def __init__(self):
        self.bullets = []
    
    def move(self):
        bullets = []
        for bullet in self.bullets:
            ret = bullet.move()
            if ret:
                bullets.append(bullet)
        
        self.bullets = bullets


    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add(self, x, y):
        self.bullets.append(Bullet(x, y))

    def kill(self, enemies):
        bullets = []
        for bullet in self.bullets:
            ix = bullet.rect.collidelist(enemies)
            if ix != -1:
                enemies.pop(ix)
            else:
                bullets.append(bullet)
        self.bullets = bullets





pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sprite Introduction")
player = pygame.Rect(0,0,50,30)
player.midbottom = screen.get_rect().midbottom
enemies = Enemies(5)
bullets = Bullets()
clock = pygame.time.Clock()

# bullets.add(250, 400)
# bullets.add(200, 400)
# bullets.add(350, 400)

while True:

    clock.tick(10) # 10 fps
    screen.fill((0, 0, 0))
    bullets.move()
    bullets.kill(enemies.enemies)
    enemies.draw(screen)
    enemies.move()
    bullets.draw(screen)
    pygame.draw.rect(screen, (0,0,255), player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x, y = player.center
                bullets.add(x, y)
    pygame.display.flip()
    

