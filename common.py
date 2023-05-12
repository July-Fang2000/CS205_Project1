class Puzzle:
    def __init__(self, size):
        self.size = size
        self.val = [[0] * size for _ in range(size)]

    def set_val(self, row, col, value):
        self.val[row][col] = value

    def to_array(self):
        array = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.val[i][j])
            array.append(row)
        return array


class Node:
    def __init__(self, puzzle, row, col):
        self.puzzle = puzzle
        self.h = 0
        self.g = 0
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.g + self.h < other.g + other.h
