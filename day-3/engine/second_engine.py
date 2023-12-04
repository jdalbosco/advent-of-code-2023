from engine.engine import Engine

class SecondEngine(Engine):
    GEAR = '*'

    def __init__(self):
        super().__init__()
        self.gears = dict()

    @staticmethod
    def create(input):
        engine = SecondEngine()
        engine.process_schematic(input, [engine.SYMBOL, engine.GEAR], "[^0-9\.*]")
        return engine
    
    def run(self):
        sum = 0
        for number in self.numbers:
            self.connect_to_gear(number)
    
        for gear in self.gears.values():
            if len(gear) == 2:
                sum += gear[0] * gear[1]

        return sum

    def add_symbol_and_continue(self, row, column):
        self.symbols.add((row, column))
        if self.schematic[row][column] == self.GEAR:
            self.gears[(row, column)] = []
        return column + 1
        
    def connect_to_gear(self, number):
        for row, column in number.get_adjacent_squares():
            if (row, column) in self.gears:
                self.gears[(row, column)].append(number.value)
