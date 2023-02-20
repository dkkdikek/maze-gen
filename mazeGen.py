
import pygame
from random import choice

#interface implementation:
res = width, height = 1000, 800
tile = 100
cols , rows = width // tile, height // tile 

pygame.init()
screen =  pygame.display.set_mode(res)
clock = pygame.time.Clock()



class Cell:

    def __init__(self,x,y):
        self.x, self.y = x, y
        self.walls = { 'top': True, 'right' : True, 'left' : True, 'bottom' : True}
        self.visited = False
    
    def draw_current_cell(self):
        x, y = self.x * tile, self.y * tile
        pygame.draw.rect(screen, pygame.Color('saddlebrown'), (x + 2, y + 2, tile - 2, tile - 2) )

    def draw(self):
        x, y = self.x * tile, self.y * tile
        if self.visited:
            pygame.draw.rect(screen, pygame.Color('black'), (x,y,tile,tile))

        if self.walls['top']:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x,y),(x + tile,y), 2)
        if self.walls['right']:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x + tile, y), (x + tile, y + tile), 2)
        if self.walls['bottom']:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x + tile, y + tile), (x, y+ tile), 2)
        if self.walls['left']:
            pygame.draw.line(screen, pygame.Color('darkorange'), (x, y + tile), (x,y), 2)

    def checkCell(self, x, y):
        pass
        
gridCells = [Cell(col, row) for row in range(rows) for col in range(cols)]
currentCell = gridCells[0]
stack = []







while True:
    screen.fill(pygame.Color('teal'))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    [cell.draw() for cell in gridCells]
    currentCell.visited = True
    currentCell.draw_current_cell()


    pygame.display.flip()
    clock.tick(30)



