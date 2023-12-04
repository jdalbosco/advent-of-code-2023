import re
from engine.engine_number import Number

class Engine():
    SYMBOL = '#'
    DIGITS = '0123456789'

    def __init__(self):
        self.schematic = []
        self.rows = 0
        self.columns = 0
        self.numbers = []
        self.symbols = set()

    def run():
        pass

    def process_schematic(self, input, possible_symbols, regex_to_normalize_engine):
        self.make_symbols_consistent(input, regex_to_normalize_engine)
        self.rows = len(self.schematic)
        self.columns = len(self.schematic[0]) - 1

        self.find_numbers_and_symbols(possible_symbols)

    def make_symbols_consistent(self, input, regex):
        for line in input:
            self.schematic.append(re.sub(regex, self.SYMBOL, line))

    def find_numbers_and_symbols(self, symbols):
        for row_idx, row in enumerate(self.schematic):
            column_idx = 0
            while column_idx < self.columns:
                if row[column_idx] in symbols:
                    column_idx = self.add_symbol_and_continue(row_idx, column_idx)
                elif row[column_idx] in self.DIGITS:
                    column_idx = self.add_number_and_continue(row_idx, column_idx, row)
                else:
                    column_idx += 1

    def add_symbol_and_continue(self, row, column):
        self.symbols.add((row, column))
        return column + 1

    def add_number_and_continue(self, row, column, engine_row):
        number = ''
        columns = []
        while column < self.columns and engine_row[column] in self.DIGITS:
            number += engine_row[column]
            columns.append(column)
            column += 1
        self.numbers.append(Number(int(number), row, columns))
        return column
