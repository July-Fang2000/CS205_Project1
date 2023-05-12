from math import sqrt
from common import *
from method import *

size = int(sqrt(int(input("Please input the number of X-puzzle:\n "
                          "(e.g. if you want to solve the 8-puzzle, you need to enter 8) \n"))+1))

puzzle = Puzzle(size)

print("input the value of puzzle, use zero to represent the blank: ")
for i in range(size):
    for j in range(size):
        puzzle.set_val(i, j, value=int(input("row {} and column {}: \n".format(i, j))))

original_puzzle = puzzle.to_array()

goal_puzzle = [[0] * puzzle.size for _ in range(puzzle.size)]
count = 1
for i in range(size):
    for j in range(size):
        goal_puzzle[i][j] = count
        count += 1
goal_puzzle[size-1][size-1] = 0




