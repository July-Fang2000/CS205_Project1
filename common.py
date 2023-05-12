class Puzzle:
    def __init__(self, size):
        self.size = size
        self.val = [[0] * size for _ in range(size)]

    def set_val(self, row, col, value):
        self.val[row][col] = value

    def get_val(self, row, col):
        return self.val[row][col]

    # def find_blank(self):
    #     for i in range(self.size):
    #         for j in range(self.size):
    #             if self.val[i][j] == 0:
    #                 return i, j
    #     return None

    def to_array(self):
        array = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.val[i][j])
            array.append(row)
        return array
