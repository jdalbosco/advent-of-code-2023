from engine.engine import Engine

class FirstEngine(Engine):
    @staticmethod
    def create(input):
        engine = FirstEngine()
        engine.process_schematic(input, [engine.SYMBOL], "[^0-9\.]")
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
