import time
import random
import os

def create_grid(width, height):
    """Creates a grid of the specified dimensions, filled with dead cells."""
    return [[0 for _ in range(width)] for _ in range(height)]

def randomize_grid(grid, density=0.2):
    """Randomly populates the grid with live cells based on the given density."""
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if random.random() < density:
                grid[row][col] = 1

def get_neighbors(grid, row, col):
    """Counts the live neighbors of a cell."""
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbor_row = row + i
            neighbor_col = col + j
            if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
                count += grid[neighbor_row][neighbor_col]
    return count

def update_grid(grid):
    """Updates the grid based on the rules of Conway's Game of Life."""
    new_grid = create_grid(len(grid[0]), len(grid))
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            neighbors = get_neighbors(grid, row, col)
            if grid[row][col] == 1: # Live cell
                if neighbors < 2 or neighbors > 3:
                    new_grid[row][col] = 0
                else:
                    new_grid[row][col] = 1
            else: # Dead cell
                if neighbors == 3:
                    new_grid[row][col] = 1
    return new_grid

def print_grid(grid):
    """Prints the grid to the console."""
    os.system('cls' if os.name == 'nt' else 'clear') # Clear console
    for row in grid:
        print(''.join(['*' if cell else ' ' for cell in row]))

if __name__ == "__main__":
    width = 40
    height = 20
    grid = create_grid(width, height)
    randomize_grid(grid, 0.2)

    while True:
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(0.1)