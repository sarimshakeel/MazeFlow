import pygame
import time
from maze_generation import draw_maze

white = (255, 255, 255)
red = (255, 0, 0)
gray = (128, 128, 128)
fps = 60

def dfs(win, grid):
    stack = [grid[0][0]]
    visited = set()
    visited.add((0, 0))
    clock = pygame.time.Clock()
    start_time = time.time()

    while stack:
        current = stack[-1]
        current.highlight(win, white)
        pygame.display.update()
        clock.tick(fps)

        if current == grid[len(grid) - 1][len(grid[0]) - 1]:
            elapsed_time = time.time() - start_time
            print(f"Maze solved in {elapsed_time:.4f} seconds.")
            return True

        neighbors = []
        row, col = current.row, current.col

        if not current.walls["top"] and (row - 1, col) not in visited:
            neighbors.append(grid[row - 1][col])
        if not current.walls["right"] and (row, col + 1) not in visited:
            neighbors.append(grid[row][col + 1])
        if not current.walls["bottom"] and (row + 1, col) not in visited:
            neighbors.append(grid[row + 1][col])
        if not current.walls["left"] and (row, col - 1) not in visited:
            neighbors.append(grid[row][col - 1])

        if neighbors:
            next_node = neighbors[0]
            visited.add((next_node.row, next_node.col))
            stack.append(next_node)
        else:
            stack.pop()

        draw_maze(win, grid)
        for node in stack:
            node.highlight(win, gray)