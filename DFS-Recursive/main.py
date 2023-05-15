#Idea for dfs recursive way: https://medium.com/@ojhasaurabh2099/traversing-a-grid-using-dfs-ac7a391f7af8 
#Gambling project

#Make 3 by 3 grid with random numbers from 1 to 9 (repetitions are allowed)
""" 
Ex:
 5    3    5    

 4    7    9    

 3    1    4    
"""

#Ask the user for a number from 1 to 9 
    #validate input validation: check if the input is an integer
    #generate the grid

#traverse the grid with dfs recursively dfs_recursion()

#If it finds the number, stop.

#add all the numbers that were traversed

#print the score

# dfs_recursive(row, col, )

import random

SCORE = 0 

#1. USER INPUT AND INPUT_VALIDATION
#size
rows = 3 
cols = 3

#There can be only numbers from 1 to max_number inclusive
max_number = 9 

my_number = input(f"Type a number from 1 to {max_number} inclusive: ")

#Check if input is an integer
if (not my_number.isnumeric()):
    print("Input is not an integer")
    exit()    

number = int(my_number)

if(number < 1 or number > max_number):
    print(f"Numbers must be from 1 to {max_number} inclusive")
    exit()

#Numbers can only be from 1 to max_number inclusive
list = [ random.sample(range(1,max_number+1), rows) for i in range(cols) ]

"""
    left    (-1, 0)
    right   (1, 0)
    up      (0, 1)
    down    (0, -1)
"""
dRow = [0, 0, 1, -1]
dCol = [-1, 1, 0, 0]

vis = [[False for i in range(cols)] for j in range(rows)]

#2. FUNCTIONS
"""
    Name: print_array
    Returns: boolean 
    Purpose: Prints the list and check if the target_number (user's number) is found. It can also print vis
    Params: one list, and one str one character (str because no calculations are involved)
"""
def print_array(arr, target_number = '0'):

    target_number_found = False
    for i in arr:
        for j in i:
            if(str(j) == target_number and target_number_found == False or str(j) == str(True)):
                print(f"\033[1;32m{j}\033[0m", '\t', end="")
                target_number_found = True
            else:
                print(j, '\t', end="")
        print("")
    
    return target_number_found

"""
   Name: is_valid 
   Returns: boolean
   Purpose: checks if the current node coordinates are not out of scope. 
   Params: node coordinates i and j, size rows x cols
"""
def is_valid(i, j, rows, cols):
    return (i >= 0 and i < rows and j >= 0 and j < cols)

"""
    Name: dfs_recursive
    Returns: A string when the target_number is found. It will stop recursion 
    Purpose: Iterates the 2D array with depth first search recursively
    Params: i and j node coordinates, rows and cols size, target_number to find to stop program
"""
def dfs_recursive(i, j, vis, rows, cols, target_number):
    global SCORE 
    global list

    #get the number from i j coordinate 
    number = list[i][j]
    #add the score
    SCORE += number

    #prints visited number
    print("Visiting:", number)
    #node visited
    vis[i][j] = True
    print_array(vis)
    print("")

    #If the number reaches target_number, stop and return the function with string
    if(str(number) == target_number):
        exit(f"Score: {SCORE}")

    for k in range(0,4):
        changeRow = i + dRow[k]
        changeCol = j + dCol[k]
        if(is_valid(changeRow, changeCol, rows, cols) and not vis[changeRow][changeCol]):
            dfs_recursive(changeRow, changeCol, vis, rows, cols, target_number)

    return SCORE

#3. PROGRAM STARTS HERE
found_number = print_array(list, my_number)

#Debugging
# print("Checking visit...")
# print_array(vis)
print("")

if(not found_number):
    print("Out of luck! Better try next time!")
    exit()

dfs_recursive(0,0, vis, rows, cols, my_number)
