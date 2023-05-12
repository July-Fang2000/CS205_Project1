from math import sqrt

from common import *
from method import *

goal_puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

size = int(sqrt(int(input("input the puzzle size: \n"))+1))
print(size)
puzzle = Puzzle(size)

for i in range(size):
    for j in range(size):
        puzzle.set_val(i, j, value=int(input("input the value of row {} and column {}: \n".format(i, j))))

blank_row, blank_col = puzzle.find_blank()
print(blank_row, blank_col)