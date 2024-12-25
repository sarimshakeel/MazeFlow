import pygame
import time
from generate import draw_maze, get_neighbors

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
        for node in stack:
            node.highlight(win, gray)

    return None

def bfs(win, grid):
    queue = deque([grid[0][0]])  # Queue holding cells to explore
    visited = set()  # Track visited cells
    visited.add((0, 0))
    parent = {}  # Track the parent of each cell to reconstruct the path
    clock = pygame.time.Clock()
    start_time = time.time()

    while queue:
        current = queue.popleft()
        if current == grid[-1][-1]:  # If the end cell is reached
            elapsed_time = time.time() - start_time
            elapsed_time = round(elapsed_time, 2)
            print(f"Maze solved in {elapsed_time:.2f} seconds.")
            return elapsed_time

        for neighbor in get_neighbors(current, grid):
            if (neighbor.row, neighbor.col) not in visited:
                queue.append(neighbor)
                visited.add((neighbor.row, neighbor.col))
                parent[(neighbor.row, neighbor.col)] = current

        draw_maze(win, grid)
        for cell in queue:
            cell.highlight(win, white)  # Highlight cells in the queue with white
        current.highlight(win, gray)  # Highlight the current cell with gray
        pygame.display.flip()
        clock.tick(fps)

    # Reconstruct the path
    current = grid[-1][-1]
    while current in parent:
        current.highlight(win, green)  # Highlight the path with green
        current = parent[(current.row, current.col)]
        pygame.display.flip()
        clock.tick(fps)

def dead_end_filling(win, grid):
    visited = set()
    visited.add((0, 0))
    stack = [grid[0][0]]
    clock = pygame.time.Clock()
    start_time = time.time()

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
        for node in stack:
            node.highlight(win, gray)

    return None

def dead_end_filling(win, grid):
    visited = set()
    clock = pygame.time.Clock()
    start_time = time.time()

    def is_dead_end(cell):
        row, col = cell.row, cell.col
        open_paths = 0
        if not cell.walls["top"] and (row - 1, col) not in visited:
            open_paths += 1
        if not cell.walls["right"] and (row, col + 1) not in visited:
            open_paths += 1
        if not cell.walls["bottom"] and (row + 1, col) not in visited:
            open_paths += 1
        if not cell.walls["left"] and (row, col - 1) not in visited:
            open_paths += 1
        return open_paths == 1

    while True:
        dead_ends = []
        for row in grid:
            for cell in row:
                if (cell.row, cell.col) not in visited and is_dead_end(cell):
                    dead_ends.append(cell)

        if not dead_ends:
            break

        for cell in dead_ends:
            visited.add((cell.row, cell.col))
            cell.highlight(win, gray)
            pygame.display.update()
            clock.tick(fps)

    # Reconstruct the path
    parent = {}
    queue = [grid[0][0]]
    visited = set()
    visited.add((0, 0))

    while queue:
        current = queue.pop(0)
        if current == grid[-1][-1]:
            break

        for neighbor in get_neighbors(current, grid):
            if (neighbor.row, neighbor.col) not in visited:
                queue.append(neighbor)
                visited.add((neighbor.row, neighbor.col))
                parent[(neighbor.row, neighbor.col)] = current

    current = grid[-1][-1]
    while current in parent:
        current.highlight(win, green)  # Highlight the path with green
        current = parent[(current.row, current.col)]
        pygame.display.flip()
        clock.tick(fps)

    elapsed_time = time.time() - start_time
    elapsed_time = round(elapsed_time, 2)
    print(f"Maze solved in {elapsed_time:.2f} seconds.")
    return elapsed_time