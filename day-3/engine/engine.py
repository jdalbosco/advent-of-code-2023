import re
from engine.number import Number

SYMBOL = '#'
GEAR = '*'
DIGITS = '0123456789'

class Engine():
    def __init__(self):
        self.schematic = []
        self.rows = 0
        self.columns = 0
        self.numbers = []
        self.symbols = set()
        self.gears = dict()

    def process_schematic(self, input):
        self.make_symbols_consistent(input)
        self.rows = len(self.schematic)
        self.columns = len(self.schematic[0]) - 1

        self.find_numbers_and_symbols()

    def make_symbols_consistent(self, input):
        for line in input:
            self.schematic.append(re.sub("[^0-9\.*]", SYMBOL, line))

    def find_numbers_and_symbols(self):
        for row_idx, row in enumerate(self.schematic):
            column_idx = 0
            while column_idx < self.columns:
                if row[column_idx] in [SYMBOL, GEAR]:
                    column_idx = self.add_symbol_and_continue(row_idx, column_idx, row[column_idx])
                elif row[column_idx] in DIGITS:
                    column_idx = self.add_number_and_continue(row_idx, column_idx, row)
                else:
                    column_idx += 1

    def add_symbol_and_continue(self, row, column, symbol):
        self.symbols.add((row, column))
        if symbol == GEAR:
            self.gears[(row, column)] = []
        return column + 1

    def add_number_and_continue(self, row, column, engine_row):
        number = ''
        columns = []
        while column < self.columns and engine_row[column] in DIGITS:
            number += engine_row[column]
            columns.append(column)
            column += 1
        self.numbers.append(Number(int(number), row, columns))
        return column
    
    def is_part_number(self, number):
        for row, column in number.get_adjacent_squares():
            if (row, column) in self.symbols:
                return True
        return False
    
    def connect_to_gear(self, number):
        for row, column in number.get_adjacent_squares():
            if (row, column) in self.gears:
                self.gears[(row, column)].append(number.value)
