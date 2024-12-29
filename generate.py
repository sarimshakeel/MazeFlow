import pygame
import random

Width, Height = 600, 600
Green = (0, 255, 0)
Black = (0, 0, 0)
Padding = 10

class Cell:
    def __init__(self, row, col, cell_size):
        self.row = row
        self.col = col
        self.cell_size = cell_size
        self.visited = False
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.children = []

    def draw(self, screen, color):
        x, y = self.col * self.cell_size + Padding, self.row * self.cell_size + Padding
        if self.walls['top']:
            pygame.draw.line(screen, color, (x, y), (x + self.cell_size, y))
        if self.walls['right']:
            pygame.draw.line(screen, color, (x + self.cell_size, y), (x + self.cell_size, y + self.cell_size))
        if self.walls['bottom']:
            pygame.draw.line(screen, color, (x + self.cell_size, y + self.cell_size), (x, y + self.cell_size))
        if self.walls['left']:
            pygame.draw.line(screen, color, (x, y + self.cell_size), (x, y))

    def highlight(self, screen, color):
        x, y = self.col * self.cell_size + Padding, self.row * self.cell_size + Padding
        pygame.draw.rect(screen, color, (x, y, self.cell_size, self.cell_size))

def create_grid(rows, cols):
    cell_size = (Width - 2 * Padding) // rows  # Adjust cell size to account for padding
    grid = [[Cell(row, col, cell_size) for col in range(cols)] for row in range(rows)]
    return grid

def get_neighbors(cell, grid):
    neighbors = []
    row, col = cell.row, cell.col
    if row > 0 and not grid[row - 1][col].visited:  
        neighbors.append(grid[row - 1][col])
    if col < len(grid[0]) - 1 and not grid[row][col + 1].visited:  
        neighbors.append(grid[row][col + 1])
    if row < len(grid) - 1 and not grid[row + 1][col].visited:
        neighbors.append(grid[row + 1][col])
    if col > 0 and not grid[row][col - 1].visited:  
        neighbors.append(grid[row][col - 1])
    return neighbors

def remove_walls(current, next):
    dx = current.col - next.col
    dy = current.row - next.row
    if dx == 1:  
        current.walls["left"] = False
        next.walls["right"] = False
    elif dx == -1:  
        current.walls["right"] = False
        next.walls["left"] = False
    elif dy == 1: 
        current.walls["top"] = False
        next.walls["bottom"] = False
    elif dy == -1: 
        current.walls["bottom"] = False
        next.walls["top"] = False    

def generate_maze(win, grid, rows, cols):
    stack = []
    current = grid[0][0]
    current.visited = True

    while True:
        neighbors = get_neighbors(current, grid)
        if neighbors:
            next_node = random.choice(neighbors)
            next_node.visited = True
            stack.append(current)
            remove_walls(current, next_node)
            current.children.append(next_node)
            current = next_node
        elif stack:
            current = stack.pop()
        else:
            break

        draw_maze(win, grid)
        pygame.display.update()

def draw_maze(win, grid):
    win.fill(Black)
    for row in grid:
        for node in row:
            node.draw(win, Green)
