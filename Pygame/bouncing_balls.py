import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Balls")

class Circle:

    def __init__(self, color, center, radius, width, hv, vv):
        self.color = color
        self.center = center
        self.radius = radius
        self.width = width

        self.hv = hv
        self.vv = vv

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius, self.width)

    def move(self):
        x, y = self.center
        x += self.hv
        y += self.vv

        if x + self.radius > screen.get_rect().width:
            x = screen.get_rect().width - self.radius
            self.hv = -self.hv
        
        elif x - self.radius < 0:
            x = self.radius
            self.hv = -self.hv

        if y + self.radius > screen.get_rect().height:
            y = screen.get_rect().height - self.radius
            self.vv = -self.vv
        elif y - self.radius < 0:
            y = self.radius
            self.vv = -self.vv
        self.center = (x, y)
        

clock = pygame.time.Clock()
circle1 = Circle((255,0,0), (100, 200), 70, 5, -10, 5)
circle2 = Circle((0,0,255), (400, 350), 70, 5, 5, -5)
click = pygame.mixer.Sound("./Pygame/click.wav")
bg_sound = pygame.mixer.Sound("./Pygame/bg_sound.wav")
# def distance(x1, y1, x2,y2):
    # return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

bg_sound.play(loops=-1)
bg_sound.set_volume(0.1)
while True:

    clock.tick(20)
    screen.fill((0,0,0))
    circle1.move()
    circle2.move()
    
    # x1, y1 = circle1.center
    # x2, y2 = circle2.center
    c1 = pygame.math.Vector2(circle1.center)
    c2 = pygame.math.Vector2(circle2.center)

    # if distance(x1, y1, x2, y2) <= 2 * circle1.radius:
    if c1.distance_to(c2) <= 2*circle1.radius:
        # screen.fill((255, 255, 255))
        normal_vector = c2 - c1

        circle1.hv, circle1.vv = pygame.math.Vector2(circle1.hv, circle1.vv).reflect(normal_vector)
        circle2.hv, circle2.vv = pygame.math.Vector2(circle2.hv, circle2.vv).reflect(normal_vector)

        click.play()

    circle1.draw(screen)
    circle2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
