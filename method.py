from common import *


def uniform_cost_search():
    cost = 0
    return cost


def a_star_with_misplaced_tile_heuristic(original_puzzle, goal_puzzle):
    distance = 0
    size = len(original_puzzle)
    for i in range(size):
        for j in range(size):
            if original_puzzle[i][j] != goal_puzzle[i][j] and original_puzzle[i][j] != 0:
                distance += 1
    return distance


def a_star_with_manhattan_distance_heuristic(original_puzzle, goal_puzzle):
    distance = 0
    size = len(original_puzzle)
    for i in range(size):
        for j in range(size):
            value = original_puzzle[i][j]
            if value != 0:
                row_goal, col_goal = divmod(goal_puzzle.index(value), size)
                distance += abs(row_goal - i) + abs(col_goal - j)
    return distance


def search(original_puzzle, goal_puzzle, solve_method):
    # find the blank position in original_puzzle
    blank_col, blank_row = 0, 0
    for i in range(len(original_puzzle)):
        for j in range(len(original_puzzle)):
            if original_puzzle[i][j] == 0:
                blank_row, blank_col = i, j

    current_puzzle = Node(original_puzzle, blank_row, blank_col)

    # use the method to get h value come from heuristic algorithm
    if solve_method == 1:
        current_puzzle.hcost = uniform_cost_search()
    elif solve_method == 2:
        current_puzzle.hcost = a_star_with_misplaced_tile_heuristic(original_puzzle, goal_puzzle)
    elif solve_method == 3:
        current_puzzle.hcost = a_star_with_manhattan_distance_heuristic(original_puzzle, goal_puzzle)
