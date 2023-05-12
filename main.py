from math import sqrt
from common import *
from method import *

# # create the arbitrary initial state X-puzzle
# size = int(sqrt(int(input("Please input the number of X-puzzle:\n "
#                           "(e.g. if you want to solve the 8-puzzle, you need to enter 8) \n"))+1))
# puzzle = Puzzle(size)
# print("input the value of puzzle, use zero to represent the blank: ")
# for i in range(size):
#     for j in range(size):
#         puzzle.set_val(i, j, value=int(input("row {} and column {}: \n".format(i, j))))
# original_puzzle = puzzle.to_array()
#
# # create the goal_puzzle of the X-puzzle problem
# goal_puzzle = [[0] * puzzle.size for _ in range(puzzle.size)]
# count = 1
# for i in range(size):
#     for j in range(size):
#         goal_puzzle[i][j] = count
#         count += 1
# goal_puzzle[size-1][size-1] = 0

# use to simple test
original_puzzle = [[0, 7, 2], [4, 6, 1], [3, 5, 8]]
goal_puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# select the method to solve the problem
solve_method = int(input('Select a method: \n'
                        '1) Uniform Cost Search. \n'
                        '2) A* with the Misplaced Tile heuristic. \n'
                        '3) A* with the Manhattan Distance heuristic.\n'
                         '(e.g. if you want to use Uniform Cost Search, enter 1)\n'))

# search the solution
search(original_puzzle, goal_puzzle, solve_method)
