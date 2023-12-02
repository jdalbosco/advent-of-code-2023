class Game():
    def __init__(self):
        self.id = None
        self.rounds = []

    def is_possible(self, bag: dict):
        for round in self.rounds:
            for color, quantity in round.items():
                if bag[color] < quantity:
                    return False
        return True
    
    def calculate_power(self) -> int:
        minimum_bag = {"red": 0, "green": 0, "blue": 0}
        
        for round in self.rounds:
            for color, quantity in round.items():
                if minimum_bag[color] < quantity:
                    minimum_bag[color] = quantity
        
        power = 1
        for quantity in minimum_bag.values():
            power *= quantity

        return power