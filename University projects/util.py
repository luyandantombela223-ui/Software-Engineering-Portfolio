# A code to manipulate 2-d arrays
# Luyanda Ntombela
# 09 May 2025

def create_grid(grid):
    """Create a 4x4 grid filled with zeroes."""
    for i in range(4):
        grid.append([0] * 4)

def print_grid(grid):
    """Print a 4x4 grid in 5-width columns inside a box."""
    print("+" + "-" * 20 + "+")
    for row in grid:
        print("|", end="")
        for num in row:
            if num == 0:
                print(" ".ljust(5), end="")
            else:
                print(str(num).ljust(5), end="")
        print("|")
    print("+" + "-" * 20 + "+")

def check_lost(grid):
    """Return True if there are no 0s and no adjacent equal values; otherwise False."""
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
    return True

def check_won(grid):
    """Return True if a value >= 32 is found in the grid; otherwise False."""
    for row in grid:
        for num in row:
            if num >= 32:
                return True
    return False

def copy_grid(grid):
    """Return a copy of the given grid."""
    return [row[:] for row in grid]

def grid_equal(grid1, grid2):
    """Check if 2 grids are equal."""
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True
