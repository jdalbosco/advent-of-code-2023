class Number():
    def __init__(self, number, row, columns):
        self.value = number
        self.row = row
        self.columns = columns

    def get_adjacent_squares(self):
        UP = self.row - 1
        DOWN = self.row + 1
        LEFT = self.columns[0] - 1
        RIGHT = self.columns[-1] + 1

        adjacent_squares = []
        
        # squares above and below number
        for column in self.columns:
            adjacent_squares.append((UP, column))
            adjacent_squares.append((DOWN, column))
        
        # squares to the left and right
        adjacent_squares.append((self.row, LEFT))
        adjacent_squares.append((self.row, RIGHT))

        # diagonal squares
        adjacent_squares.append((UP, LEFT))
        adjacent_squares.append((DOWN, LEFT))
        adjacent_squares.append((UP, RIGHT))
        adjacent_squares.append((DOWN, RIGHT))

        return adjacent_squares
