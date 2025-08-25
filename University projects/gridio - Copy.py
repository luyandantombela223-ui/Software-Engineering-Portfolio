# Finding the missing number if it is present
# Luyanda Ntombela
# 22 March 2025 
# Program: gridio.py
# Purpose: Allows a user to input a 9x9 integer grid and query values using coordinates.
# Author: Luyanda (Your Name)
# Date: March 22, 2025

# Function to read a 9x9 grid from user input
def read_grid():
    grid = []  # Initialize an empty list to store the grid
    print("Enter an array:")
    for _ in range(9):  # Loop to read 9 rows
        row = input()  # Get each row as a string
        grid.append([int(digit) for digit in row])  # Convert each digit to an integer and add to grid
    return grid

# Function to query the grid based on user input coordinates
def query_grid(grid):
    while True:
        # Prompt for coordinates
        coords = input("Enter coordinates:\n")
        x, y = map(int, coords.split())  # Split input and convert to integers

        # Check for termination
        if x == -1 or y == -1:
            print("DONE")
            break

        # Validate the coordinates
        if x < 0 or x >= 9 or y < 0 or y >= 9:
            print("Invalid coordinates. Please enter values between 0 and 8.")
        else:
            # Print the value at the specified coordinates
            print("Value =", grid[x][y])

# Main function to execute the program
if __name__ == "__main__":
    grid = read_grid()  # Read the grid from user input
    query_grid(grid)  # Start querying the grid
