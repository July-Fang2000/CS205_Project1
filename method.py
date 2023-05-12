def uniform_cost_search():
    cost = 0
    return cost


def a_star_with_misplaced_tile_heuristic(current_puzzle, goal_puzzle):
    distance = 0
    size = len(current_puzzle)
    for i in range(size):
        for j in range(size):
            if current_puzzle[i][j] != goal_puzzle[i][j] and current_puzzle[i][j] != 0:
                distance += 1
    return distance


def a_star_with_manhattan_distance_heuristic(current_puzzle, goal_puzzle):
    distance = 0
    size = len(current_puzzle)
    for i in range(size):
        for j in range(size):
            value = current_puzzle[i][j]
            if value != 0:
                row_goal, col_goal = divmod(goal_puzzle.index(value), size)
                distance += abs(row_goal - i) + abs(col_goal - j)
    return distance

def search(original_puzzle, goal_puzzle, method):
