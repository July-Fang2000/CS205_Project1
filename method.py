import copy
import heapq
import sys
import time

from common import *


def uniform_cost_search():
    cost = 0
    return cost


def a_star_with_misplaced_tile_heuristic(original_puzzle, goal_puzzle):
    # calculate the misplaced between the original puzzle and the goal puzzle
    misplaced = 0
    size = len(original_puzzle)
    for i in range(size):
        for j in range(size):
            if original_puzzle[i][j] != goal_puzzle[i][j] and original_puzzle[i][j] != 0:
                misplaced += 1
    return misplaced


def a_star_with_manhattan_distance_heuristic(original_puzzle, goal_puzzle):
    # calculate the Manhattan distance between the original puzzle and the goal puzzle
    distance = 0
    size = len(original_puzzle)
    goal_dict = {}
    # create a dictionary to map the goal values to their respective locations
    for i in range(size):
        for j in range(size):
            goal_dict[goal_puzzle[i][j]] = (i, j)
    # calculate the Manhattan distance for each value in the original puzzle
    for i in range(size):
        for j in range(size):
            value = original_puzzle[i][j]
            if value != 0:
                row_goal, col_goal = goal_dict[value]
                distance += abs(row_goal - i) + abs(col_goal - j)
    return distance


def search(original_puzzle, goal_puzzle, solve_method):
    start = time.time()

    # find the blank position in original_puzzle
    blank_col, blank_row = 0, 0
    for i in range(len(original_puzzle)):
        for j in range(len(original_puzzle)):
            if original_puzzle[i][j] == 0:
                blank_row, blank_col = i, j

    current_puzzle = Node(original_puzzle, blank_row, blank_col)

    # use the method to get h value come from heuristic algorithm
    if solve_method == 1:
        current_puzzle.h = uniform_cost_search()
    elif solve_method == 2:
        current_puzzle.h = a_star_with_misplaced_tile_heuristic(original_puzzle, goal_puzzle)
    elif solve_method == 3:
        current_puzzle.h = a_star_with_manhattan_distance_heuristic(original_puzzle, goal_puzzle)

    queue = [current_puzzle]  # use heapq as the data structure
    old_puzzle = [original_puzzle]  # record the visited puzzle
    count = -1  # count expand node number
    max_queue = 0  # count the queue size
    tol = 200  # time limit

    while True:
        # if no more nodes can test, this puzzle problem can't solve.
        if len(queue) == 0:
            print("Can't solve this puzzle!")
            return 0

        # get and pop the first puzzle in the heap queue
        q = heapq.heappop(queue)
        count += 1

        # if it gets the goal, end the loop
        if q.puzzle == goal_puzzle:
            print("Depth was: " + str(q.g))
            print("Node expand number: " + str(count))
            print("max queue size: " + str(max_queue))
            print("Running time: " + str(time.time() - start) + "seconds")
            return "Solve this puzzle"

        # print the current puzzle being explored
        print("The best state to expand with a g(n) = " + str(q.g) + " and h(n) = "
              + str(q.h) + " is...\n" + str(q.puzzle) + "\n")

        # expand and get its four neighbors of the node
        new_puzzle = generate_puzzle(q, old_puzzle)

        # update the g and h of each algorithm
        for i in new_puzzle:
            if solve_method == 1:
                i.g = q.g + 1
                i.h = uniform_cost_search()
            elif solve_method == 2:
                i.g = q.g + 1
                i.h = a_star_with_misplaced_tile_heuristic(i.puzzle, goal_puzzle)
            elif solve_method == 3:
                i.g = q.g + 1
                i.h = a_star_with_manhattan_distance_heuristic(i.puzzle, goal_puzzle)
            if i.puzzle not in old_puzzle:
                heapq.heappush(queue, i)
                old_puzzle.append(i.puzzle)

        # update the max_queue size
        if len(queue) > max_queue:
            max_queue = len(queue)

        #  end the program if time limit exceed
        if time.time() > start + tol:
            print('Time Limit Exceeded')
            sys.exit()


def generate_puzzle(current_puzzle, old_puzzle):
    move_puzzle = []
    row, col = current_puzzle.row, current_puzzle.col
    direction = [1, 0, -1, 0, 1]  # defines the directions: right, down, left, up
    for i in range(0, 4):
        current = copy.deepcopy(current_puzzle.puzzle)  # create a deep copy of the current puzzle
        temp = current[row][col]  # temporarily store the value at the current position
        r = row + direction[i]  # calculate the new row position
        c = col + direction[i + 1]  # calculate the new column position
        if r < 0 or r > len(current) - 1 or c < 0 or c > len(current) - 1:
            continue  # if the new position is out of bounds, skip to the next direction
        current[row][col] = current[r][c]  # move the value from the new position to the current position
        current[r][c] = temp  # move the temporarily stored value to the new position
        if current is not None and current not in old_puzzle:
            # check if the new puzzle state is valid and not already explored
            nodes = Node(current, r, c)  # create a new Node with the new puzzle state and position
            move_puzzle.append(nodes)  # add the new Node to the list of neighboring puzzles
    return move_puzzle
