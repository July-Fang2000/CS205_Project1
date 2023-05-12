class Puzzle:
    def __init__(self, size):
        # Initialize the puzzle with a given size
        self.size = size
        self.val = [[0] * size for _ in range(size)]  # 2D array to represent the puzzle

    def set_val(self, row, col, value):
        # Set the value of a specific position in the puzzle
        self.val[row][col] = value

    def to_array(self):
        # Convert the puzzle to a 2D array format and return it
        array = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.val[i][j])
            array.append(row)
        return array


class Node:
    def __init__(self, puzzle, row, col):
        # Initialize a node with a puzzle state, row and column position
        self.puzzle = puzzle
        self.h = 0  # heuristic value
        self.g = 0  # cost to reach this node from the start node
        self.row = row  # row position of the empty tile in the puzzle
        self.col = col  # column position of the empty tile in the puzzle

    def __lt__(self, other):
        # Compare two nodes based on their g+h values
        return self.g + self.h < other.g + other.h
