import pygame
import sys
import time

def draw_grid(surface):
    pygame.draw.line(surface, (0,0,0), (200, 0), (200, 600), 5)
    pygame.draw.line(surface, (0,0,0), (400, 0), (400, 600), 5)
    pygame.draw.line(surface, (0,0,0), (0, 200), (600, 200), 5)
    pygame.draw.line(surface, (0,0,0), (0, 400), (600, 400), 5)


def get_grid_pos(pos):
    x, y = pos

    #first column
    if x <= 200 and y <= 200:
        return (0,0), 0, 0
    if x <= 200 and y <= 400:
        return (1,0), 200, 0
    if x <= 200 and y <= 600:
        return (2,0), 400, 0

    #second column
    if x <= 400 and y <= 200:
        return (0,1), 0, 200
    if x <= 400 and y <= 400:
        return (1,1), 200, 200
    if x <= 400 and y <= 600:
        return (2,1), 400, 200
    
    #third column
    if x <= 600 and y <= 200:
        return (0,2), 0, 400
    if x <= 600 and y <= 400:
        return (1,2), 200, 400
    if x <= 600 and y <= 600:
        return (2,2), 400, 400
    
def check_win(symbol):
    
    for i in range(3):
        if grid[i][0] == symbol and grid[i][1] == symbol and grid[i][2] == symbol:
            return True
        if grid[0][i] == symbol and grid[1][i] == symbol and grid[2][i] == symbol:
            return True
    
    if grid[0][0] == symbol and grid[1][1] == symbol and grid[2][2] == symbol:
        return True
    
    if grid[0][2] == symbol and grid[1][1] == symbol and grid[2][0] == symbol:
        return True
    
    return False
        



pygame.init()
screen = pygame.display.set_mode((600, 600))
dot = pygame.image.load("C:\\Users\\Manu\\Desktop\\DG_Lectures\\Pygame\\dot.bmp")
dot = pygame.transform.scale(dot, (200, 200))

cross = pygame.image.load("C:\\Users\\Manu\\Desktop\\DG_Lectures\\Pygame\\cross.bmp")
cross = pygame.transform.scale(cross, (200, 200))

font = pygame.font.SysFont(None, 60)

images = [dot, cross]

grid = [[None,None,None], [None,None,None], [None,None,None]]

rectangles = []
move = 0
pause = False
game_win = False

while True:

    screen.fill((255, 255, 255))
    for (rect, i) in rectangles:
        screen.blit(images[i], rect)
    draw_grid(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not pause:
            grid_loc, top, left = get_grid_pos(event.pos)
            i, j = grid_loc
            if grid[i][j] == None:
                rect = pygame.Rect(left, top, 200, 200)
                rectangles.append((rect, move))
                grid[i][j] = move
                move = 1 - (move == 1)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                grid = [[None,None,None], [None,None,None], [None,None,None]]
                rectangles = []
                move = 0
                pause = False
                game_win = False


    if check_win(0) and not pause:
        font_image = font.render("Dot Won", True, (255, 0, 0), (255,255,255))
        font_rect = font_image.get_rect()
        font_rect.center = screen.get_rect().center
        pause = True
        game_win = True
    
    if check_win(1) and not pause:
        font_image = font.render("Cross Won", True, (255, 0, 0), (255,255,255))
        font_rect = font_image.get_rect()
        font_rect.center = screen.get_rect().center
        pause = True
        game_win = True
    if game_win:
        screen.blit(font_image, font_rect)
    pygame.display.flip()

