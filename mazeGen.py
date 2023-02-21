
import pygame
from random import choice
 # from entities import Cell

#interface implementation:
res = width, height = 1000, 800
tile = 30
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
        findIndex = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return gridCells[findIndex(x,y)]
    
    def checkNeighbors(self):
        neighbors = []
        top = self.checkCell(self.x,self.y - 1)
        right = self.checkCell(self.x + 1, self.y)
        bottom = self.checkCell(self.x, self.y + 1)
        left = self.checkCell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False






def removeWalls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False




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

    nextCell = currentCell.checkNeighbors()
    if nextCell:
        nextCell.visited = True
        stack.append(currentCell)
        removeWalls(currentCell,nextCell)
        currentCell = nextCell
    elif stack:
        currentCell = stack.pop()

    pygame.display.flip()
    clock.tick(200)



