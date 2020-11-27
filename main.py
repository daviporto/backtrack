import pygame
from cell import Cell
from colors import hexToRGB

pygame.init()

BACKGROUND_COLOR = hexToRGB(0x783de2)
WIDTH, HEIGHT = 900, 500
FRAME_RATE = 600
Cell.WIDTH, Cell.HEIGHT = WIDTH, HEIGHT 
Title = 'backtrack maze generation'
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(Title)

for y in range(HEIGHT // Cell.height):
    for x in range(WIDTH // Cell.width):
        Cell.cells.append(Cell(x, y))

stack = []
current = Cell.cells[0]
current.visited = True
stack.append(current)
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FRAME_RATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    nextCell = current.get_neighbor()
    if nextCell:
        stack.append(nextCell)
        nextCell.visited = True
        current.removeWall(nextCell)
        current = nextCell
    elif len(stack):
        current = stack.pop()
        

    screen.fill(BACKGROUND_COLOR)
    for c in Cell.cells:
        c.draw(screen)

    for cell in stack:
        cell.on_stack(screen)
        
    current.highlight(screen)
    pygame.display.update()
