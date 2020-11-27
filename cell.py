import random
import pygame
from colors import hexToRGB
class Cell:
    width = 10
    height = 10
    color = (0, 0, 0)
    visitedColor = hexToRGB(0x1e31d8)
    highlight_color = hexToRGB(0xe71303)
    stack_color = hexToRGB(0x12e252)
    cells = []

    @staticmethod
    def index_valid(x, y):
        if x < 0 or y < 0 or x >= Cell.WIDTH // Cell.width or y >= Cell.HEIGHT // Cell.height:
            return False
        else:
            # print(
                # f"x = {x}, Y = {y}, = {x + y * (Cell.WIDTH // Cell.width)}, len = {len(Cell.cells)}")
            return Cell.cells[x + y * Cell.WIDTH // Cell.width]

    def __init__(self, x, y):
        self.x = x * Cell.width
        self.y = y * Cell.height
        self.index_x = x
        self.index_y = y
        self.walls = [True, True, True, True]
        self.visited = False

    def removeWall(self, other):
        x = self.index_x - other.index_x
        y = self.index_y - other.index_y

        if x == -1:
            self.walls[1] = False
            other.walls[3] = False
        elif x == 1:
            self.walls[3] = False
            other.walls[1] = False
        elif y == -1:
            self.walls[0] = False
            other.walls[2] = False
        elif y == 1:
            self.walls[2] = False
            other.walls[0] = False

    def get_neighbor(self):
        top = Cell.index_valid(self.index_x, self.index_y - 1)
        right = Cell.index_valid(self.index_x + 1, self.index_y)
        bottom = Cell.index_valid(self.index_x, self.index_y + 1)
        left = Cell.index_valid(self.index_x - 1, self.index_y)

        not_visited_neighbors = []
        if top and not top.visited:
            not_visited_neighbors.append(top)

        if right and not right.visited:
            not_visited_neighbors.append(right)

        if bottom and not bottom.visited:
            not_visited_neighbors.append(bottom)

        if left and not left.visited:
            not_visited_neighbors.append(left)

        if not_visited_neighbors:
            return not_visited_neighbors[random.randint(0, len(not_visited_neighbors) - 1)]
        else:
            return False
        
    def draw_rec(self, screen, color):
        pygame.draw.rect(screen, color, pygame.Rect(
            self.x, self.y, Cell.width, Cell.height))

    def draw(self, screen):
        if self.visited:
            self.draw_rec(screen, Cell.visitedColor)
            
        if self.walls[0]:
            pygame.draw.line(screen, Cell.color, (self.x, self.y),
                             (self.x + Cell.width, self.y))
        if self.walls[1]:
            pygame.draw.line(screen, Cell.color, (self.x + Cell.width,
                                                  self.y), (self.x + Cell.width, self.y + Cell.height))
        if self.walls[2]:
            pygame.draw.line(screen, Cell.color, (self.x, self.y +
                                                  Cell.height), (self.x + Cell.width, self.y + Cell.height))
        if self.walls[3]:
            pygame.draw.line(screen, Cell.color, (self.x, self.y),
                             (self.x, self.y + Cell.height))

        
    def on_stack(self, screen):
        self.draw_rec(screen, Cell.stack_color)

    def highlight(self, screen):
        self.draw_rec(screen, Cell.highlight_color)
        