class Number():
    def __init__(self, number, row, columns):
        self.value = number
        self.row = row
        self.columns = columns

    def get_adjacent_squares(self):
        up = self.row - 1
        down = self.row + 1
        left = self.columns[0] - 1
        right = self.columns[-1] + 1

        adjacent_squares = []
        
        # squares above and below number
        for column in self.columns:
            adjacent_squares.append((up, column))
            adjacent_squares.append((down, column))
        
        # squares to the left and right
        adjacent_squares.append((self.row, left))
        adjacent_squares.append((self.row, right))

        # diagonal squares
        adjacent_squares.append((up, left))
        adjacent_squares.append((down, left))
        adjacent_squares.append((up, right))
        adjacent_squares.append((down, right))

        return adjacent_squares
