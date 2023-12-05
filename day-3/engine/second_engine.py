from engine.engine import Engine

GEAR = '*'

class SecondEngine(Engine):
    def __init__(self):
        super().__init__()
        self.gears = dict()

    @staticmethod
    def create(input):
        engine = SecondEngine()
        for line in input:
            engine.schematic.append(line)
        engine.process_schematic(GEAR)
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
        self.gears[(row, column)] = []
        return column + 1

    def connect_to_gear(self, number):
        for row, column in number.get_adjacent_squares():
            if (row, column) in self.gears:
                self.gears[(row, column)].append(number.value)
