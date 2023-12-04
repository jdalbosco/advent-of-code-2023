class Scratchcard():
    def __init__(self, card_number, winning_numbers, scratched_numbers):
        self.number = card_number
        self.winning_numbers = winning_numbers
        self.scratched_numbers = scratched_numbers

    def calculate_points(self) -> int:
        matching_numbers = self.winning_numbers.intersection(self.scratched_numbers)
        return int(2 ** (len(matching_numbers) - 1))
    
    def number_of_matches(self) -> int:
        matching_numbers = self.winning_numbers.intersection(self.scratched_numbers)
        return len(matching_numbers)
    
    def calculate_copied_cards(self) -> list:
        return [(self.number + offset + 1) for offset in range(self.number_of_matches())]
