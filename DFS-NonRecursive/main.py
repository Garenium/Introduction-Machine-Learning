
#Sources:
# https://www.geeksforgeeks.org/depth-first-traversal-dfs-on-a-2d-array/
# https://www.youtube.com/watch?v=QxY16bI37oc 
from typing import List 
import random

def print_array(arr):
    for i in arr:
        for j in i:
            if(j == True):
                print(f"\033[1;32m {j}\033[0m", '\t', end="")
            else:
                print(j, '\t', end="")
        print("")

ROWS = random.randint(1,10) 
COLS = random.randint(1,10) 
print(f"Size {ROWS} X {COLS}")

target_row = random.randint(0,ROWS-1)
print(f"Row {target_row}")
target_col = random.randint(0,COLS-1)
print(f"Column {target_col}")

# print(f"Coordinate for True: {random_row}, {random_col}\n")

arr = [ [False]*COLS for i in range(ROWS) ]

arr[target_row][target_col] = True

print_array(arr)
print("\n")

"""
    left (-1, 0)
    right (0, 1)
    down (1,0)
    up (-1,0)
"""

dRow = [0, 0, 1, -1]
dCol = [-1, 1, 0, 0]
vis = [[False for i in range(COLS)] for j in range(ROWS)]

def isValid(row, col):
    global ROWS
    global COLS
    global vis
    
    # If cell is out of bounds
    if (row < 0 or col < 0 or row >= ROWS or col >= COLS):
        return False

    # If the cell is already visited
    if (vis[row][col]):
        return False

    # Otherwise, it can be visited
    return True


def dfs_non_recursive(row, col, grid):
    global dRow
    global dCol
    global vis
    
    # Initialize a stack of pairs and
    # push the starting cell into it
    current = []
    current.append([row, col])

    # Iterate until the
    # stack is not empty
    while (len(current) > 0):
        # Pop the top pair
        curr = current[len(current) - 1]
        current.remove(current[len(current) - 1])
        row = curr[0]
        col = curr[1]

        # Check if the current popped
        # cell is a valid cell or not
        if (isValid(row, col) == False):
            continue

        if (row == target_row and col == target_col and grid[row][col] == True):
           return f"\nFound True {row},{col}"

        # Mark the current
        # cell as visited
        vis[row][col] = True

        # Print the element at
        # the current top cell
        print(f"{grid[row][col]}:", f"{row},{col}")

        # Push all the adjacent cells
        for i in range(4):
            adjx = row + dRow[i]
            adjy = col + dCol[i]
            current.append([adjx, adjy])

print(dfs_non_recursive(0,0,arr))
