import re
from engine.engine import Engine

SYMBOL = '#'

class FirstEngine(Engine):
    @staticmethod
    def create(input):
        engine = FirstEngine()
        for line in input:
            engine.schematic.append(re.sub("[^0-9\.]", SYMBOL, line))
        engine.process_schematic(SYMBOL)
        return engine
    
    def run(self):
        sum = 0
        for number in self.numbers:
            if self.is_part_number(number):
                sum += number.value
        return sum
            
    def is_part_number(self, number):
        for row, column in number.get_adjacent_squares():
            if (row, column) in self.symbols:
                return True
        return False
