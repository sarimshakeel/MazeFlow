import pygame
import time
from generate import draw_maze, get_neighbors
from collections import deque

green = (0, 255, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (128, 128, 128,128)
fps = 60

def dfs(win, grid):
    stack = [grid[0][0]]
    visited = set()
    visited.add((0, 0))
    clock = pygame.time.Clock()
    start_time = time.time()

    highlight_surface = pygame.Surface((win.get_width(), win.get_height()), pygame.SRCALPHA)

    while stack:
        current = stack[-1]
        current.highlight(win, white)
        pygame.display.update()
        clock.tick(fps)

        if current == grid[len(grid) - 1][len(grid[0]) - 1]:
            elapsed_time = time.time() - start_time
            elapsed_time = round(elapsed_time, 3)
            print(f"Maze solved in {elapsed_time:.4f} seconds.")
            return elapsed_time

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
        highlight_surface.fill((0, 0, 0, 0))
        for node in stack:
            node.highlight(highlight_surface, gray)
        win.blit(highlight_surface, (0, 0))
        pygame.display.flip()

    return None

def bfs(screen, grid):
    start = grid[0][0]
    end = grid[-1][-1]
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        current = queue.popleft()

        # Visualize the current cell being visited
        current.highlight(screen, white)
        pygame.display.update()
        pygame.time.delay(50)

        if current == end:
            break

        for neighbor in current.children:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

                # Highlight neighbors being added to the queue
                neighbor.highlight(screen, blue)

    # Trace back the path
    path = []
    while end is not None:
        path.append(end)
        end = parent[end]
    path.reverse()

    for cell in path:
        cell.highlight(screen, red)
        pygame.display.update()
        pygame.time.delay(100)

    return len(path)

def dead_end_filling(win, grid):
    rows, cols = len(grid), len(grid[0])
    clock = pygame.time.Clock()

    # Highlight surface for visualization
    highlight_surface = pygame.Surface((win.get_width(), win.get_height()), pygame.SRCALPHA)

    start_time = time.time()  # Start timing

    while True:
        dead_ends = []

        # Identify all dead-end cells (cells with exactly one open wall)
        for row in grid:
            for cell in row:
                open_walls = sum(not cell.walls[direction] for direction in cell.walls)
                if open_walls == 1 and cell != grid[0][0] and cell != grid[rows - 1][cols - 1]:
                    dead_ends.append(cell)

        if not dead_ends:
            break  # Exit when no more dead ends exist

        # Fill in the dead ends
        for cell in dead_ends:
            for direction, is_wall in cell.walls.items():
                if not is_wall:
                    if direction == "top":
                        neighbor = grid[cell.row - 1][cell.col]
                    elif direction == "right":
                        neighbor = grid[cell.row][cell.col + 1]
                    elif direction == "bottom":
                        neighbor = grid[cell.row + 1][cell.col]
                    elif direction == "left":
                        neighbor = grid[cell.row][cell.col - 1]

                    # Close the wall between the cell and its neighbor
                    cell.walls[direction] = True
                    neighbor.walls["bottom" if direction == "top" else
                                   "left" if direction == "right" else
                                   "top" if direction == "bottom" else
                                   "right"] = True
                    break

        # Visualization
        draw_maze(win, grid)
        highlight_surface.fill((0, 0, 0, 0))  # Clear the highlight surface
        for cell in dead_ends:
            cell.highlight(highlight_surface, white)
        win.blit(highlight_surface, (0, 0))
        pygame.display.flip()
        clock.tick(fps)
        pygame.time.delay(100)

    # Highlight the remaining path with red
    for row in grid:
        for cell in row:
            if any(not cell.walls[direction] for direction in cell.walls):
                cell.highlight(win, red)
    pygame.display.update()

    elapsed_time = time.time() - start_time  # Calculate elapsed time
    print(f"Dead-end filling completed in {elapsed_time:.4f} seconds.")
